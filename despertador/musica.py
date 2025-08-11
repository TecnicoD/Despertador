import pygame, time
pygame.mixer.pre_init(frequency=48000,size=16,channels=2,buffer=512)
pygame.mixer.init()
pygame.mixer.music.load("Desktop\despertador\musica.wav")

#time.sleep(5) #tiempo es por segundos haber como le hacemos
def empezar1():
    pygame.mixer.music.play()

    parar=(int(input("pulse 1 para parar:     ")))
    if parar== 1:
        pygame.mixer.music.stop()

    while pygame.mixer.music.get_busy():
        pass

    seguir=int(input("pulse 1 para seguir:    "))
    if seguir== 1:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass


#Horas= int("0")
#Minutos= int("0")
#segundos= int("0")

def empezar2 ():

    Horas = (int(input("CUANTAS HORAS PRECISA:          ")))
    Minutos = (int(input("CUANTOS MINUTOS PRECISA:     ")))
    segundos= (int(input("CUANTOS SEGUNDOS PRECISA:     ")))
    while Horas >= 0:
    
        while (Minutos >= 0):
        
            while (segundos >= 0):
            
                print("")
                print(Horas,":", Minutos, ":",segundos)
                time.sleep(1); # Espera 1 segundo
                segundos-= 1
            
            segundos = int("59") 
            Minutos-= 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        
        Minutos = 59
        Horas-= 1
    
    print("")
    print("Fin")
    empezar1()



##ACCION


empezar2()