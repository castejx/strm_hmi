from pickle import FALSE
from select import select
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import json
import streamlit.components.v1 as components  
from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
from datetime import datetime
from pycomm3 import SLCDriver
with SLCDriver('192.168.0.100') as drive:

	def buttonHoras():
		for i, selectbox in enumerate(buttons_l):
			if selectbox == "Sí":
				cad="N150:"+str(d)+"/"+ str(i)
				drive.write((cad, 1))
			else:
				cad="N150:"+str(d)+"/"+ str(i)
				drive.write((cad, 0))
	
	def buttonTemp():
		for i, number_input in enumerate(temps):
			a=punto_dia_t+i
			cad="N150:"+ str(a) 
			#st.write(number_input)	
			drive.write((cad, number_input))

	def buttonCircuito():
		for i, selectbox in enumerate(circs):
			a=punto_dia_c+i
			cad="N150:"+ str(a)
			if selectbox=='Ninguno':
				r=0
			elif selectbox=='Todos':
				r=1
			elif selectbox=='C1':
				r=2
			elif selectbox=='C2':
				r=3
			elif selectbox=='C3':
				r=4
			elif selectbox=='C4':
				r=5
			elif selectbox=='C1+C2':
				r=6
			elif selectbox=='C1+C3':
				r=7
			elif selectbox=='C1+C4':
				r=8
			elif selectbox=='C2+C3':
				r=9
			elif selectbox=='C2+C4':
				r=10
			elif selectbox=='C3+C4':
				r=11
			elif selectbox=='C1+C2+C3':
				r=12
			elif selectbox=='C1+C2+C4':
				r=13
			elif selectbox=='C1+C3+C4':
				r=14
			elif selectbox=='C2+C3+C4':
				r=15

			drive.write((cad, r))
		
	def mostrarTemperaturas():

		txt_t=['Oficina','Baño inf.','Baño sup','Calle','Cocina','Dormitorio 1','Dormitorio 2','Dormitorio PPAL','Planta 1','Planta 2','Salita','Salon']
		plc_temps=[]
		plc_temps_aux=[]
		
		plc_temps_aux=plc_temps
		sumatoria_temp=0	
		for i in range(12):
			plc_temps.append(drive.read("F15:"+str(i))[1])
			sumatoria_temp=sumatoria_temp+plc_temps[i]
		
				#st.write(plc_temps[i])
		with st.expander("Temperaturas"):
			col1, col2, col3,col4 = st.columns(4)	

			col1.metric(txt_t[0], str(round(plc_temps[0],2))+"°C")
			col2.metric(txt_t[1], str(round(plc_temps[1],2))+"°C")
			col3.metric(txt_t[2], str(round(plc_temps[2],2))+"°C")
			col4.metric(txt_t[3], str(round(plc_temps[3],2))+"°C")

			col1.metric(txt_t[4], str(round(plc_temps[4],2))+"°C")
			col2.metric(txt_t[5], str(round(plc_temps[5],2))+"°C")
			col3.metric(txt_t[6], str(round(plc_temps[6],2))+"°C")
			col4.metric(txt_t[7], str(round(plc_temps[7],2))+"°C")

			col1.metric(txt_t[8], str(round(plc_temps[8],2))+"°C")
			col2.metric(txt_t[9], str(round(plc_temps[9],2))+"°C")
			col3.metric(txt_t[10], str(round(plc_temps[10],2))+"°C")
			col4.metric(txt_t[11], str(round(plc_temps[11],2))+"°C")
			col4.metric('Media',str(round(sumatoria_temp/12))+"°C")

	def buttonC1Values():
		for i, number_input in enumerate(values_c1):
			a=i
			cad="N252:"+ str(a) 
			#st.write(number_input)	
			drive.write((cad, number_input))

	def buttonC2Values():
		for i, number_input in enumerate(values_c2):
			a=i+5
			cad="N252:"+ str(a) 
			#st.write(number_input)	
			drive.write((cad, number_input))

	def buttonC3Values():
		for i, number_input in enumerate(values_c3):
			a=i+10
			cad="N252:"+ str(a) 
			#st.write(number_input)	
			drive.write((cad, number_input))

	def buttonC4Values():
		for i, number_input in enumerate(values_c4):
			a=i+15
			cad="N252:"+ str(a) 
			#st.write(cad)	
			drive.write((cad, number_input))

	


	count = st_autorefresh(interval=100000, limit=100, key="fizzbuzzcounter")
	st.write(f"Count: {count}")

	if count == 99:
		count=0

		
	#if count%2 ==0:
	
		#now = datetime.now()
		#fecha=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
		#hora=str(now.hour)+":"+str(now.minute)
		#with open("v1.txt","a") as file:
		#	d='{date:\"'+fecha+' - '+hora+'\" pv:\"'+str(drive.read("N30:1")[1])+'\" cv:\"'+str(drive.read("F15:0")[1])+'\"}'
		#	file.write(d)
			
		


			



	st.header("Control Utilities Casa")
	

	tab1, tab2, tab3, tab4,tab5 = st.tabs(["Principal","Programacion diaria", "Resumen","Circuitos","Graficas"])

	

	with st.sidebar:
		selected = option_menu(
			menu_title="Principal",
			options=["Home","Projects","Contact"])
		
		st.title("Hora PLC")	
		st.write(str(drive.read("N11:2")[1]/100))
		

	#if selected=="Home":
	#	st.title("Principal")
	#if selected=="Projects":
	#	st.title("Projects")

	
	with tab1:
		st.header("Principal")
	
		
		
		mostrarTemperaturas()
		
		
		

			

		
		components.html("<html><body><hr></body></html>", width=200, height=200)
	
	txt=["00:00","01:30","03:00","04:30","06.00","07:30","09:00","10:30","12:00","13:30","15:00","16:30","18:00","19:30","21:00","22:30"]

	with tab2:

		if False:
			st.error('REAL TIME ACTIVADO', icon="🚨")
			#real_time=False
			#st.write(real_time)
		else:
		
			dia = st.select_slider('Día de la semana',options=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
			
			if dia == 'Lunes':
				d=0
			elif dia == 'Martes':
				d=1
			elif dia == 'Miercoles':
				d=2
			elif dia == 'Jueves':
				d=3
			elif dia == 'Viernes':
				d=4
			elif dia == 'Sabado':
				d=5
			elif dia == 'Domingo':
				d=6
		


			puntero_t=119
			puntero_c=7

			punto_dia_t=(d*16)+puntero_t
			punto_dia_c=(d*16)+puntero_c

			st.header(dia)

			col1h, col1t, col1c = st.columns(3)
			with col1h:
				st.subheader("Hora")
				buttons_l=[]
				value_plc=0
				for i in range(16):
		   			cad="N150:"+str(d)+"/"+ str(i)
		   			#st.write('C', cad)

		   			if (drive.read(cad)[1])==True:
		   				value_plc=1
		   			else:
		   				value_plc=0
	   				buttons_l.append(st.selectbox(txt[i],('No','Sí'),key=cad,index=value_plc))

		
			

			with col1t:
				st.subheader("Temp. Cº")
				temps=[]
				for i in range(16):
		   			a=punto_dia_t+i
		   			cad="N150:"+ str(a)  		
		   			temps.append(st.number_input(txt[i],value=drive.read(cad)[1],key=a))

		
			with col1c:
				st.subheader("Circuito")
				circs=[]
				for i in range(16):
		   			a=punto_dia_c+i
		   			cad="N150:"+ str(a)  
		   			#st.write(cad)		
		   			circs.append(st.selectbox(txt[i],('Ninguno','Todos','C1','C2','C3','C4','C1+C2','C1+C3','C1+C4','C2+C3','C2+C4','C3+C4','C1+C2+C3','C1+C2+C4','C1+C3+C4','C2+C3+C4'),key=a,index=drive.read(cad)[1]))
			
		if st.button('Guardar',key="guardar_circ"):
			buttonCircuito()
			buttonHoras()
			buttonTemp()

		
	with tab3:
		colL, colM, colX, colJ, colV, colS, colD = st.columns(7)
		with colL:
			st.subheader("L")
			checks_l=[]
			value_plc=False
			d=0
			for i in range(16):
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_l.append(st.checkbox(txt[i],value=value_plc,key='l'+cad))

			for i, checkbox in enumerate(checks_l):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))

		with colM:
			st.subheader("M")
			checks_m=[]
			value_plc=False
			d=1
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_m.append(st.checkbox(txt[i],value=value_plc,key='m'+cad))

			for i, checkbox in enumerate(checks_m):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	    			#st.write(cad)
		with colX:
			st.subheader("X")
			checks_x=[]
			value_plc=False
			d=2
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_x.append(st.checkbox(txt[i],value=value_plc,key='x'+cad))

			for i, checkbox in enumerate(checks_x):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	    			#st.write(cad)
		with colJ:
			st.subheader("J")
			checks_j=[]
			value_plc=False
			d=3
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_j.append(st.checkbox(txt[i],value=value_plc,key='j'+cad))

			for i, checkbox in enumerate(checks_j):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	    			#st.write(cad)
		with colV:
			st.subheader("V")
			checks_v=[]
			value_plc=False
			d=4
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_j.append(st.checkbox(txt[i],value=value_plc,key='v'+cad))

			for i, checkbox in enumerate(checks_v):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	    			#st.write(cad)

		with colS:
			st.subheader("S")
			checks_s=[]
			value_plc=False
			d=5
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_s.append(st.checkbox(txt[i],value=value_plc,key='s'+cad))

			for i, checkbox in enumerate(checks_s):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	    			#st.write(cad)

		with colD:
			st.subheader("D")
			checks_d=[]
			value_plc=False
			d=6
			for i in range(16):	
		   		cad="N150:"+str(d)+"/"+ str(i)
		   		if (drive.read(cad)[1])==True:
		   			value_plc=True
		   			#st.write(cad)
		   		else:
		   			value_plc=False

	   			checks_d.append(st.checkbox(txt[i],value=value_plc,key='d'+cad))

			for i, checkbox in enumerate(checks_d):
			    if checkbox:
			    	cad="N150:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    	#st.write(cad)
			    	#st.write(f"{i} checkbox was clicked")
			    else:
	    			cad="N150:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))
	

	

	with tab4:
		txt_circuitos=["Circuito 1","Circuito 2","Circuito 3","Circuito 4","ON AUTO"]
		txt_gen=["AUTO/MAN","Paro general","Termostato habilitado","Orden termostato"]
		txt_circ=["Circuito ON AUTO","Manual","Forzado","PID MAN","Funcionado"]
		txt_v_circ=["TD","TI","KC","SPS","TF"]
		with st.expander("P&Id"):
			image = Image.open('pid.jpg')
			st.image(image)

		colV1, colV2, colV3, colV4 = st.columns(4)
		with colV1:
			st.subheader("Circuito 1")
			checks_c1=[]
			value_plc=False
			d=7
			if drive.read("B180:7/0")[1]:
				st.success('Seleccionado', icon="✅")
			else:
				st.warning('No selecc.', icon="⚠️")
			if drive.read("B180:7/4")[1]:
				st.success('En marcha', icon="✅")
			else:
				st.warning('Parado', icon="⚠️")



			for i in range(4):	
				
				cad="B180:"+str(d)+"/"+ str(i)
				if (drive.read(cad)[1])==True:
					value_plc=True
					#st.write(cad)
				else:
					value_plc=False

			
				checks_c1.append(st.checkbox(txt_circ[i],value=value_plc,key='C1'+cad))

			for i, checkbox in enumerate(checks_c1):
			    if checkbox:
			    	cad="B180:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    else:
	    			cad="B180:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))

			with st.expander("PID"):
				values_c1=[]
				for i in range(5):
					a=0+i
					cad="N252:"+ str(a)  
					values_c1.append(st.number_input(txt_v_circ[i],value=drive.read(cad)[1],key="c1"+str(a)))

				if st.button('Guardar',key="guardar_c1"):
					if drive.read("B180:7/3")[1]==False:
						st.error('PID no en manual', icon="🚨")
					else:
						buttonC1Values()

			st.metric("PV:", str(round(drive.read("F8:2")[1],2))+"°C","_X̅ ciruito")
			st.metric("CV:", str(round(drive.read("N30:1")[1],2))+"%","V1")


		with colV2:
			st.subheader("Circuito 2")
			checks_c2=[]
			value_plc=False
			d=9
			if drive.read("B180:9/0")[1]:
				st.success('Seleccionado', icon="✅")
			else:
				st.warning('No selecc.', icon="⚠️")
			if drive.read("B180:9/4")[1]:
				st.success('En marcha', icon="✅")
			else:
				st.warning('Parado', icon="⚠️")

			for i in range(4):	
				
				cad="B180:"+str(d)+"/"+ str(i)
				if (drive.read(cad)[1])==True:
					value_plc=True
					#st.write(cad)
				else:
					value_plc=False

			
				checks_c2.append(st.checkbox(txt_circ[i],value=value_plc,key='C2'+cad))

			for i, checkbox in enumerate(checks_c2):
			    if checkbox:
			    	cad="B180:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    else:
	    			cad="B180:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))

			with st.expander("PID"):
				values_c2=[]
				for i in range(5):
					a=5+i
					cad="N252:"+ str(a)  
					values_c2.append(st.number_input(txt_v_circ[i],value=drive.read(cad)[1],key="c2"+str(a)))

				if st.button('Guardar',key="guardar_c2"):
					if drive.read("B180:9/3")[1]==False:
						st.error('PID no en manual', icon="🚨")
					else:
						buttonC2Values()
			
			st.metric("PV:", str(round(drive.read("F8:6")[1],2))+"°C","_X̅ ciruito")
			st.metric("CV:", str(round(drive.read("N32:1")[1],2))+"%","V2")

		with colV3:
			st.subheader("Circuito 3")
			checks_c3=[]
			value_plc=False
			d=10
			if drive.read("B180:10/0")[1]:
				st.success('Seleccionado', icon="✅")
			else:
				st.warning('No selecc.', icon="⚠️")
			if drive.read("B180:10/4")[1]:
				st.success('En marcha', icon="✅")
			else:
				st.warning('Parado', icon="⚠️")

			for i in range(4):	
				
				cad="B180:"+str(d)+"/"+ str(i)
				if (drive.read(cad)[1])==True:
					value_plc=True
					#st.write(cad)
				else:
					value_plc=False

			
				checks_c3.append(st.checkbox(txt_circ[i],value=value_plc,key='C3'+cad))

			for i, checkbox in enumerate(checks_c3):
			    if checkbox:
			    	cad="B180:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    else:
	    			cad="B180:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))

			with st.expander("PID"):
				values_c3=[]
				for i in range(5):
					a=10+i
					cad="N252:"+ str(a)  
					values_c3.append(st.number_input(txt_v_circ[i],value=drive.read(cad)[1],key="c3"+str(a)))

				if st.button('Guardar',key="guardar_c3"):
					if drive.read("B180:10/3")[1]==False:
						st.error('PID no en manual', icon="🚨")
					else:
						buttonC3Values()

			st.metric("PV:", str(round(drive.read("F8:8")[1],2))+"°C","_X̅ ciruito")
			st.metric("CV:", str(round(drive.read("N34:1")[1],2))+"%","V3")

		with colV4:
			st.subheader("Circuito 4")
			checks_c4=[]
			value_plc=False
			d=11
			if drive.read("B180:11/0")[1]:
				st.success('Seleccionado', icon="✅")
			else:
				st.warning('No selecc.', icon="⚠️")
			if drive.read("B180:11/4")[1]:
				st.success('En marcha', icon="✅")
			else:
				st.warning('Parado', icon="⚠️")


			for i in range(4):	
				
				cad="B180:"+str(d)+"/"+ str(i)
				if (drive.read(cad)[1])==True:
					value_plc=True
					#st.write(cad)
				else:
					value_plc=False

			
				checks_c4.append(st.checkbox(txt_circ[i],value=value_plc,key='C4'+cad))

			for i, checkbox in enumerate(checks_c4):
			    if checkbox:
			    	cad="B180:"+str(d)+"/"+ str(i)
			    	drive.write((cad, 1))
			    else:
	    			cad="B180:"+str(d)+"/"+ str(i)
	    			drive.write((cad, 0))

			with st.expander("PID"):
				values_c4=[]
				for i in range(5):
					a=15+i
					cad="N252:"+ str(a)  
					values_c4.append(st.number_input(txt_v_circ[i],value=drive.read(cad)[1],key="c4"+str(a)))

				if st.button('Guardar',key="guardar_c4"):
					if drive.read("B180:11/3")[1]==False:
						st.error('PID no en manual', icon="🚨")
					else:
						buttonC4Values()

			st.metric("PV:", str(round(drive.read("F8:10")[1],2))+"°C","_X̅ ciruito")
			st.metric("CV:", str(round(drive.read("N36:1")[1],2))+"%","V4")

	with tab5:
		#chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a','b','c'])
		#st.line_chart(chart_data)
		


		#d={'pv:':v1_pv,'cv:':v1_cv}
		#chart_data =  pd.DataFrame(data=d)
		#st.line_chart(chart_data)

	

		#with open('v1.txt', 'r') as f:
		#	data = json.load(f)

		## Output: {'name': 'Bob', 'languages': ['English', 'French']}
		#st.write(data)


		st.metric("PV:", str(round(drive.read("F15:0")[1],2))+"°C","Oficina")
		st.metric("CV:", str(round(drive.read("N30:1")[1],2))+"%","V1")





#streamlit hello
#streamlit run hmi.py