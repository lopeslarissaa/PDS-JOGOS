    import forca
    import adivinhaçao
    
    def escolher_jogo():
        print("*******************************")
        print("*******Escolha seu jogo!*******")
        print("*******************************")
        
        print("(1) forca (2) adivinhaçao")
        
        jogo = int(input("Qual o jogo?"))
        
        if(jogo == 1):
            print("jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("jogando adivinhaçao")
            adivinhaçao.jogar
            
    if(__name__ == "__main__"):
        escolhe_jogo()