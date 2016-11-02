
class Diccionario():
    """ 
    Clase que contiene los string necesarios para inicializar los datos..
        
    @author: Ismael Tobar Garcia
    @version: 1.0    
    """
    def __init__(self):
        #Estadisticas      
        self.v='v'
        self.h='h'
        self.md='md'
        self.dm='dm'
        self.totales='totales'
        self.proyec="proyect"
        self.d1="docu1"
        self.d2="docu2"
        self.d3="docu3"
        self.d4="docu4"
        self.d5="docu5"

        #Configuracion a xml
        self.tex='tex'
        self.tab='/Tabla.tex'
        self.csv='csv'
        self.sal_estad='/Salida_Estadisticas.csv' 
        self.sal_lin='/Salida_Lineas.csv' 
        self.jpg1='jpg1'
        self.origi='/Original.jpg'
        self.jpg2='jpg2'
        self.pintada='/Pintada.jpg'
        self.pro_xml="/Proyecto.xml"
        self.utf='UTF-8'
        
        #datosTo csv
        self.cabecera_csv_lineas=['linea', 'angulo', 'tamano', 'tipo']
        self.cabecera_csv_estad=['tipo', 'numero', 'mediaLon', 'desviacionTip']
        
        
        #Informe
        self.jin_blo='\BLOCK{'
        self.jin_o_q='}'
        self.jin_va=r'\VAR{' 
        self.jin_alm='\#{'
        self.jin_porc='%%'
        self.jin_alm_po='%#'
        self.infor_plan='proyecto/codigo/informes/jinja-test.tex'
        self.tab_in='Tabla.tex'
        
        
        #ProcesadoImagen
        self.jpg="JPEG"
        self.pro_img="/imagen.png"
        self.pro_img_tesse="/imagen.png "
        self.pro_tessera="/tesseract/tesseract.exe "
        self.pro_sal="/salida "
        self.pro_batch="nobatch digits "
        self.pro_sal_txt='/salida.txt'
        
        
        #MediadorPestannas
        self.md_pe_lin_pin="Lineas pintadas"
        self.md_pe_calc='Calcular Lineas'        
        self.md_pe_corre="Corregir lineas"
        self.md_pe_auto="Automatico"
        self.md_pe_corre='Corregir Lineas'
        self.md_pe_anadir_p='Anadir punto'
        self.md_pe_anadir_seg='Anadir segmentos'
        self.md_pe_borrar='Borrar seleccionado'
        self.md_pe_guardar='Guardar tabla'
        self.md_pe_limpiar='Limpiar tabla'
        self.md_pe_p1="P_1:"
        self.md_pe_p2="P_2:"
        self.md_pe_cero="0"
        self.md_pe_cero="0"
        self.md_pe_cero="0"
        self.md_pe_cero="0"
        self.md_pe_cabe_tab=['P1X', 'P1Y', 'P2X', 'P2Y']
        self.md_pe_fig_lin='Figura con lineas'
        self.md_pe_amarillo='yellow'
        self.md_pe_color_bl='color: black'
        self.md_pe_color_red='color: Red'
        self.md_pe_but_press='button_press_event'
        self.md_pe_ok="OK"
        self.md_pe_msg_sob="¿Esta seguro de sobreescribir?"
        self.md_pe_msg_inf="La carpeta ya existe"
        self.md_pe_msg_avi="Aviso"
        self.md_pe_open="openFolder"
        self.md_pe_proy='/Proyecto'
        self.md_pe_war="Warning:"
        self.md_pe_ori='/Proyecto/Original.jpg'
        self.md_pe_pin='/Proyecto/Pintada.jpg'
        self.md_pe_pro='/Proyecto/Proyecto.xml'
        self.md_pe_est='/Proyecto/Salida_Estadisticas.csv'
        self.md_pe_err_st="Falla porque esta abierto el archivo Salida_Estadisticas"
        self.md_pe_lin='/Proyecto/Salida_Lineas.csv'
        self.md_pe_err_lin="Falla porque esta abierto el archivo Salida_Lineas"
        self.md_pe_tab='/Proyecto/Tabla.tex'
        self.md_pe_err_tab="Falla porque esta abierto el archivo Tabla"
        self.md_pe_msg_gur="No se han guardado los cambios."
        
        #mediadorVentana
        self.md_v_figsin='Figura sin lineas'
        self.md_v_figcon='Figura con lineas'
        self.md_v_ori='nearest'
        self.md_v_up='upper'
        self.md_v_color='b'
        
        #VentanaInicio
        self.ini_log='logger.log'
        self.ini_nuevo="&Nuevo proyecto"
        self.ini_o_nuevo="Ctrl+O"
        self.ini_p_abrir='Abrir imagen'
        self.ini_abrir_pro="&Abrir proyecto"
        self.ini_o_abrir_pro="Ctrl+A"
        self.ini_p_abrir_pro='Abrir Proyecto'
        self.ini_salir="&Salir"
        self.ini_o_salir="Ctrl+E"
        self.ini_p_salir='Salir'
        self.ini_guardar="&Guardar proyecto"
        self.ini_o_guardar="Ctrl+G"
        self.ini_p_guardar='Guardar csv y .tex'
        self.ini_acerca="&Acerca de"
        self.ini_o_ayuda='Ayuda'
        self.ini_ayuda="&Ayuda"
        self.ini_archivo='&Archivo'
        self.ini_msg="Cargar imagen para iniciar"
        self.ini_color='color: red'
        self.ini_time="Times"        
        self.ini_msg_acerca="Autores: \n\tIsmael Tobar García \n\tAlvar Gonzalez Arnaiz\n\tJose Francisco Diez Pastor\nVersion: \n\t1.0 "
        self.ini_acercade="Acerca de"  
        self.ini_p_abri='Abrir imagen'
        self.ini_p_dir='c:/'
        self.ini_p_opt="Image files (*.jpg )"
        self.ini_p_war="Warning:"
        self.ini_p_err="Error:"
        self.ini_p_ok="OK"
        self.ini_p_cambios="Se han detectado cambios desea guardar"
        self.ini_p_aviso="Aviso"
        self.ini_p_cargar="Cargar Proyecto"
        self.ini_p_war_amp="Warning: fichero csv no existe"