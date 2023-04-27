import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import React, {createContext, useEffect, useState, useRef} from 'react';
import {BASE_URL, WS} from '../config';
import 'react-native-get-random-values';
import { v4 as uuidv4 } from 'uuid';
import * as Device from 'expo-device';
import * as forge from 'node-forge'
import * as FileSystem from 'expo-file-system';
import { wrapper } from 'axios-cookiejar-support';
import { CookieJar } from 'tough-cookie';
import { Platform, AppState } from "react-native";
import * as Notifications from 'expo-notifications';
//import BackgroundTask from 'react-native-background-task';

export const AuthContext = createContext();

var jar = new CookieJar();
axios.defaults.withCredentials = true
var client = wrapper(axios.create({ jar }));

Notifications.setNotificationHandler({
	handleNotification: async () => ({
	  shouldShowAlert: true,
	  shouldPlaySound: true,
	  shouldSetBadge: true,
	}),
  });

async function schedulePushNotification(title, subtitle, body, id) {
	await Notifications.scheduleNotificationAsync({
	  content: {
		title: title,
		subtitle:subtitle,
		body: body,
		data:{
			id:id
		},
		sound: 'newSale.mp3'
	  },
	  trigger: null,
	});
  }
  
  async function registerForPushNotificationsAsync() {
	let token;
  
	if (Platform.OS === 'android') {
	  await Notifications.setNotificationChannelAsync('default', {
		name: 'default',
		importance: Notifications.AndroidImportance.MAX,
		vibrationPattern: [0, 250, 250, 250],
		lightColor: '#FF231F7C',
	  });
	}
  
	if (Device.isDevice) {
	  const { status: existingStatus } = await Notifications.getPermissionsAsync();
	  let finalStatus = existingStatus;
	  if (existingStatus !== 'granted') {
		const { status } = await Notifications.requestPermissionsAsync();
		finalStatus = status;
	  }
	  if (finalStatus !== 'granted') {
		alert('Failed to get push token for push notification!');
		return;
	  }
	  token = (await Notifications.getExpoPushTokenAsync()).data;
	  console.log(token);
	} else {
	  alert('Must use physical device for Push Notifications');
	}
  
	return token;
  }

export const AuthProvider = ({children}) => {

	const appState = useRef(AppState.currentState);
	const [appStateVisible, setAppStateVisible] = useState(appState.current)

	useEffect(() => {
		
		const subscription = AppState.addEventListener("change", nextAppState => {
		appState.current = nextAppState;
		setAppStateVisible(appState.current);
		setStateVisible(appState.current)
		console.log("AppState", appState.current);
		if (appState.current=='active'){
			writeToDB()
		}
		if(appState.current=='background'){
			// setscrollend([serverMessagesWb.length,false])
			
		}
		});
		

		return () => {
			subscription.remove();
		}
	}, []);

	const [expoPushToken, setExpoPushToken] = useState('');
	const [notification, setNotification] = useState(false);
	const notificationListener = useRef();
	const responseListener = useRef();

	useEffect(() => {
		registerForPushNotificationsAsync().then(token => setExpoPushToken(token));
	
		notificationListener.current = Notifications.addNotificationReceivedListener(notification => {
		  setNotification(notification);
		});
	
		responseListener.current = Notifications.addNotificationResponseReceivedListener(response => {
		  console.log(response);
		});
	
		return () => {
		  Notifications.removeNotificationSubscription(notificationListener.current);
		  Notifications.removeNotificationSubscription(responseListener.current);
		};
	  }, []);


	const [userInfo, setUserInfo] = useState(false);
	const [uid, setUid] = useState({});
	const [isLoading, setIsLoading] = useState(false);
	const [splashLoading, setSplashLoading] = useState(false);
	const [loadCheckUserName, setloadCheckUserName] = useState(false);
	const [connectWS, setConnectWS] = useState(false);
	const [loadUser, setLoadUser] = useState(false);
	const [stateVisible, setStateVisible] = useState(false);
	const [filter, setFilters] = useState(false);

	const [serverMessagesWb, setServerMessagesWb] = useState([]);
	const [serverMessagesOz, setServerMessagesOz] = useState([]);
	const [serverMessagesDm, setServerMessagesDm] = useState([]);

	const [activationWB,setActivationWB] = useState(false);
	const [dataWB,setDataWb] = useState(
		{
			numWB:null,
			name:'',
			pvz:[],
			paysWB:[],
			percentAmount:[],
			limitPostaPaid:0,
			debit:0,
			percentDiscount:0
		}
		);


	
	let headerWB= async ()=>{
		let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		return ({headers:{
			'Wb-AppType': Platform.OS,
			'Wb-AppVersion': '485',
			'WB-AppLanguage': 'ru',
			'devicename': Device.modelName,
			'deviceId': ui.replace('-','').replace('-','').slice(0,16),
			'serviceType': 'FB',
			'User-Agent': 'okhttp/4.10.0',
			'X-ClientInfo': 'appType=32&curr=rub&dest=-1029256,-102269,-1252558,-1250619&emp=0&locale=ru&pricemarginCoeff=1&reg=0&regions=1,4,22,30,31,33,38,40,48,64,66,68,69,70,71,75,80,83&spp=0&sppFixGeo=4&timestamp=1668507174&lang=ru&version=4',
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		withCredentials: true
	})
	}
	const getActivationWB = async ()=>{
		let r5 = await client.get('https://home-service.wildberries.ru/home-service/api/v1/home', headerWB)

		console.log(`Activation WB ${r5.data.data.isAuthenticated}`)
		setActivationWB(r5.data.data.isAuthenticated)

		if(r5.data.data.isAuthenticated){
			setIsLoading(true);
			let dataWBc = { ...dataWB }

			let r6 = await client.get('https://napi.wildberries.ru/api/cabinet', headerWB)
			dataWBc.numWB = r6.data.data.cabinetModel.phoneMobile
			dataWBc.name = r6.data.data.cabinetModel.firstName
			dataWBc.percentDiscount = r6.data.data.cabinetModel.menu[7].text
			
			let r7 = await client.get('https://checkout-bt.wildberries.ru/checkout/api/v3/user/payments/list', headerWB)
			
			r7.data.payments.map((i,index)=>dataWBc.paysWB.push({
				key:index,
				value:i.cardMask
			}))
			//dataWBc.paysWB.push(r7.data.payments)

			dataWBc.limitPostaPaid = r7.data.settings.postpaid.limit

			let r8 = await client.get('https://home-service.wildberries.ru/home-service/api/v2/postpaid', headerWB)
			dataWBc.debit = r8.data.debit

			let r9 = await client.get('https://marketing-info.wildberries.ru/marketing-info/api/v5/info?curr=rub', headerWB)
			dataWBc.percentAmount = [r9.data.purchasePercent, r9.data.boughtSum]

			let r10 = await client.get('https://points-bt.wildberries.ru/delivery-points-storage/api/v1/user/points', headerWB)
			let ar=[]
			for (let point in r10.data.points) {
				if (r10.data.points[point].isActive) {
					ar.push(r10.data.points[point])
				}
			}
			dataWBc.pvz=ar

			setDataWb(dataWBc)
			console.log(dataWBc)
			setIsLoading(false);
		}
	}

	var ws = useRef(null)
	
	
	const check_ws = async () =>{
		const serverMessagesListWb = [];
		const serverMessagesListOz = [];
		const serverMessagesListDm = [];
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}
		

		let connect=()=>{
			ws.current = new WebSocket(WS+ui)
			

			ws.current.onopen = ()=>{
				console.log('OPEN')
				setConnectWS(true)
			}
			ws.current.onclose = (e)=>{
				setConnectWS(false)
				console.log('CLOSE')
				console.log('Сервер перезагрузился')
				setTimeout(function() {
					connect();
				}, 2000);
			}

			ws.current.onmessage = (e) =>{
				let data=JSON.parse(e.data)
				if(data.type=='sale'){
					
					for(let sale of data.dataApp){
						
						if(sale.marketplace=='wb' || sale.marketplace=='wb1'){
							let chek_sklad=sale.sklad.split(' | ')
							let skladWB=0
							let skladProd=0
							if (chek_sklad.length>1){
								skladWB=parseInt(chek_sklad[0].match(/\d+/))
								skladProd=parseInt(chek_sklad[1].match(/\d+/))
							}else{
								if (chek_sklad[0].includes('WB')){
									skladWB=parseInt(chek_sklad[0].match(/\d+/))
								}else{
									skladProd=parseInt(chek_sklad[0].match(/\d+/))
								}
							}

							

							if (filter[sale.subject][0]){
								if (filter[sale.subject][1]<=sale.price && sale.price<filter[sale.subject][2]){
									if(sale.col>=filter[sale.subject][3]){
										if(filter[sale.subject][4]){
											
											serverMessagesListWb.push(sale);
											setServerMessagesWb([... serverMessagesListWb])


											let smile='🤑'
											let diapaz=''
											if (sale.diapazmin!=null){
												diapaz=`↔️ Диапазон: ${sale.diapazmin}₽ - ${sale.diapazmax}₽`
												if (sale.price<sale.diapazmin){
													smile='📉'}
												else if(sale.price<=sale.diapazmax && sale.price>=sale.diapazmin){
													smile='📊'}
												else {smile='📈'}
											}
											let title=`🛍 ${sale.name}`
											let subtitle=`${smile} ${sale.price}₽`

											let body=`${sale.sklad.replace('<b>','').replace('</b>','').replace('<b>','').replace('</b>','')}\n${diapaz}`
											schedulePushNotification(title, subtitle, body, sale.article)
											
										}else{
											
											if (skladWB>=filter[sale.subject][3]){
												serverMessagesListWb.push(sale);
												//schedulePushNotification()
												setServerMessagesWb([... serverMessagesListWb])
											}
										}
									}
								}
								
							}
							
						}else if(data.data.marketplace=='oz'){
							serverMessagesListOz.push(data.data);
							setServerMessagesOz([... serverMessagesListOz])
						}else if(data.data.marketplace=='dm'){
							serverMessagesListDm.push(data.data);
							setServerMessagesDm([... serverMessagesListDm])
						}
					}
				}else if (data.type=='edit message'){
					
					if(data.data.marketplace=='wb'){
						serverMessagesListWb.find((o, i) => {
							if(o.id === data.data.id){
								serverMessagesListWb[i]=data.data
							}
						})
						setServerMessagesWb([... serverMessagesListWb])
					}
					
				}
				
	
			}
		}
		
		if(!connectWS){
			connect()
		}

		
		
	}

	const _0x51cec8=_0x1d4a;(function(_0x33edde,_0x19f636){const _0xf6e6a2=_0x1d4a,_0x5f4725=_0x33edde();while(!![]){try{const _0x2c4296=-parseInt(_0xf6e6a2(0xd5))/0x1+parseInt(_0xf6e6a2(0xd1))/0x2+parseInt(_0xf6e6a2(0xc6))/0x3*(-parseInt(_0xf6e6a2(0xd3))/0x4)+-parseInt(_0xf6e6a2(0xc9))/0x5*(-parseInt(_0xf6e6a2(0xcd))/0x6)+-parseInt(_0xf6e6a2(0xcc))/0x7+parseInt(_0xf6e6a2(0xce))/0x8*(parseInt(_0xf6e6a2(0xdc))/0x9)+parseInt(_0xf6e6a2(0xd0))/0xa*(parseInt(_0xf6e6a2(0xcf))/0xb);if(_0x2c4296===_0x19f636)break;else _0x5f4725['push'](_0x5f4725['shift']());}catch(_0x32af9f){_0x5f4725['push'](_0x5f4725['shift']());}}}(_0x6ae5,0x2e033));const d=require('../animations/animau.json'),animau=forge['pki']['publicKeyFromPem'](forge[_0x51cec8(0xc8)][_0x51cec8(0xd8)](d['layers'][0xc][_0x51cec8(0xd2)][0x0]['it'][0x1]['o']['ix']));function _0x6ae5(){const _0x5f30aa=['1956051NnTBSO','817671bmspLj','create','util','230905FxqmOO','encrypt','RSA-OAEP','2584155REPjzB','18mEPVWq','8stNYJV','561VRKYzi','80070AHKCZH','752356jrqhtW','shapes','4yZIEmS','trunc','310228wojjvt','now','modelName','decode64','sha256','encode64','getTimezoneOffset'];_0x6ae5=function(){return _0x5f30aa;};return _0x6ae5();}let timestampUTCNow=()=>{const _0x4f9efa=_0x51cec8;return Math[_0x4f9efa(0xd4)](Date[_0x4f9efa(0xd6)]()/0x3e8)+new Date()[_0x4f9efa(0xdb)]()/0x3c*0x3c*0x3c;};function _0x1d4a(_0x185d6b,_0x4c744d){const _0x6ae559=_0x6ae5();return _0x1d4a=function(_0x1d4ab3,_0x15cc38){_0x1d4ab3=_0x1d4ab3-0xc6;let _0xe15d31=_0x6ae559[_0x1d4ab3];return _0xe15d31;},_0x1d4a(_0x185d6b,_0x4c744d);}const lotg=(ui)=>{const _0xc13210=_0x51cec8;let _0x500e60=ui+','+timestampUTCNow(),_0x55e6ff=animau[_0xc13210(0xca)](_0x500e60,_0xc13210(0xcb),{'md':forge['md'][_0xc13210(0xd9)][_0xc13210(0xc7)](),'mgf1':forge['mgf1'][_0xc13210(0xc7)]()}),_0x488e48=forge[_0xc13210(0xc8)][_0xc13210(0xda)](_0x55e6ff);return _0x488e48;};let data=async(ui)=>{const _0x10747e=_0x51cec8;return{'z':''+lotg(ui),'ts':timestampUTCNow(),'phone':Device[_0x10747e(0xd7)],'ipv4':await getIp()};};

	const upload_avatar = async (imaged) =>{
		setIsLoading(true);
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}

		let heder = {
			headers: {
				'Content-Type': 'multipart/form-data',
				Authorization: 'TOKEN LGxfJDMPTFSlzfc0QMdO'
			}
		}
		
		const base64 = await FileSystem.readAsStringAsync(imaged.uri, { encoding: 'base64' });
		

		const im = {
			image: base64,
			name: '1'
		}

		
		const res = await axios.post(`https://api.imageban.ru/v1`, im, heder)
		

		let header = {
			headers: {
				accept: 'application/json'
			}
		}

		const upload = await axios.post(`${BASE_URL}/auth/uploadfile?url=${res.data.data.link}`, await data(ui), header)

		console.log(upload.data)
		
		writeToDB()
		setIsLoading(false);
	}

	const updateName = async (firstname, lastname, username) =>{
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}

		let header = {
			headers: {
				accept: 'application/json'
			}
		}

		
		const upload = await axios.post(`${BASE_URL}/auth/setuserinfo?firstname=${firstname}&lastname=${lastname}&username=${username}`, await data(ui), header)

		console.log(upload.data)
		writeToDB()
		
	}
	
	const writeToDB = async () => {
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}
		
		let heder = {
			headers: {
				accept: 'application/json'
			}
		}
		
		const res = await axios.post(`${BASE_URL}/auth/sign-up`, await data(ui), heder)
		
		if (res.data.tid!=null){
			setUserInfo(res.data);
			AsyncStorage.setItem('userInfo', JSON.stringify(res.data));
			console.log('load User')
			setLoadUser(true)
			
			
		}else if(res.data.detail=='Authorized without tid'){
			AsyncStorage.removeItem('userInfo');
			setUserInfo({});
			console.log('Authorized without tid')


		}else if(res.data.detail=='not uid'){
			console.log('not uid')
		}
		
		
	};

	const getIp = async () => {
		const res = await axios.get('http://ip-api.com/json/')
		
		return res.data.query
	}

	const logout = async () => {
		setSplashLoading(true);
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}
		let heder = {
			headers: {
				accept: 'application/json'
			}
		}
		
		
		const res = await axios.post(`${BASE_URL}/auth/logout`, await data(ui), heder)
		console.log(res.data)

		AsyncStorage.removeItem('userInfo');
		ws.current = null
		setUserInfo({});
		setLoadUser(false)
		setSplashLoading(false);
	};

	const check_username = async (username) => {
		setloadCheckUserName(true)
		var ui=null
		if(uid.uid==null){
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			ui=uuid.uid
		}else{
			ui=uid.uid
		}
		let heder = {
			headers: {
				accept: 'application/json'
			}
		}

		
		const res = await axios.post(`${BASE_URL}/auth/checkusername?username=${username}`, await data(ui), heder)
		setloadCheckUserName(false)
		return res.data

	};

	const isLoggedIn = async () => {
		await getActivationWB()
		try {
			setSplashLoading(true);

			let userInfo = await AsyncStorage.getItem('userInfo');
			userInfo = JSON.parse(userInfo);

			if (userInfo) {
				setUserInfo(userInfo)
			} 
			let uuid = await AsyncStorage.getItem('uid');
			uuid = JSON.parse(uuid);
			
			if (uuid!=null) {
				let tuid={
					uid:uuid.uid,
					time:timestampUTCNow(),
					phone:Device.modelName,
					ipv4: await getIp()
				}
				AsyncStorage.setItem('uid',JSON.stringify(tuid))
				setUid(tuid)
			}else{
				let uuid={
					uid:uuidv4(),
					time:timestampUTCNow(),
					phone:Device.modelName,
					ipv4: await getIp()
				}
				AsyncStorage.setItem('uid',JSON.stringify(uuid))
				setUid(uuid)
			}

			setSplashLoading(false);

			
		} catch (e) {
			setSplashLoading(false);
			console.log(`is logged in error ${e}`);
		}
	};

	const loadFilters = async () => {
		
		let filters = await AsyncStorage.getItem('loadFilters');
		filters = JSON.parse(filters);
		
		
		if (filters==null) {
			let ff={"Мужчинам":[true,0,30000,1,true],"Женщинам":[true,0,30000,1,true],"Детям":[true,0,30000,1,true],"Все для девочек":[true,0,30000,1,true],"Все для мальчиков":[true,0,30000,1,true],"Дом":[true,0,30000,1,true],"Красота":[true,0,30000,1,true],"Аксессуары":[true,0,30000,1,true],"Электроника":[true,0,30000,1,true],"Игрушки":[true,0,30000,1,true],"Мебель":[true,0,30000,1,true],"Товары для взрослых":[true,0,30000,1,true],"Продукты":[true,0,30000,1,true],"Бытовая техника":[true,0,30000,1,true],"Зоотовары":[true,0,30000,1,true],"Спорт":[true,0,30000,1,true],"Автотовары":[true,0,30000,1,true],"Книги":[true,0,30000,1,true],"Ювелирные изделия":[true,0,30000,1,true],"Для ремонта":[true,0,30000,1,true], "Сад и дача":[true,0,30000,1,true],"Здоровье":[true,0,30000,1,true],"Канцтовары":[true,0,30000,1,true],"Другое":[true,0,30000,1,true]}
			AsyncStorage.setItem('loadFilters',JSON.stringify(ff))
			setFilters(ff)
		}else{
			setFilters(filters)
		}
	
	};
	
	

	const [isLoggedInCalled, setIsLoggedInCalled] = useState(false);
	const [loadFiltersCalled, setLoadFiltersCalled] = useState(false);
	const [connectWSCalled, setConnectWSCalled] = useState(false);

	useEffect(() => {
		const fetchData = async () => {
		if (!isLoggedInCalled) {
			console.log('load is logged');
			await isLoggedIn();
			setIsLoggedInCalled(true);
		}
		};

		fetchData();
	}, [isLoggedInCalled]);

	useEffect(() => {
		const fetchData = async () => {
		if (!loadFiltersCalled && isLoggedInCalled) {
			console.log('load FILTERS');
			await loadFilters();
			setLoadFiltersCalled(true);
			
		}
		};

		fetchData();
	}, [isLoggedInCalled, loadFiltersCalled]);

	useEffect(() => {
		const fetchData = () => {
		if (!connectWSCalled && loadFiltersCalled) {
			console.log('Connection WS');
			check_ws();
			setConnectWSCalled(true);
		}
		};

		fetchData();
	}, [loadFiltersCalled, connectWSCalled]);
	
	
	
	return (
		<AuthContext.Provider
			value={{
				isLoading,
				userInfo,
				splashLoading,
				lotg,
				logout,
				writeToDB,
				uid,
				upload_avatar,
				updateName,
				check_username,
				loadCheckUserName,
				serverMessagesWb,
				serverMessagesOz,
				serverMessagesDm,
				filter,
				setFilters,
				activationWB,
				setActivationWB,
				dataWB,
				setDataWb,
				getActivationWB, 
				stateVisible, 
				setStateVisible
			}}>
			{children}
		</AuthContext.Provider>
	);
};
