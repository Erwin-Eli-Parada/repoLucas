def calcular (b, h, recub, fc, fy, Mu):
    #CALCULO DE SECCION DE ACERO A FLEXION
    Mu = Mu/1000
    d = h-recub
    dp = recub
    gamma = 0.85
    eu = 0.003
    Es = 200e3
    texto = ["","","",""]

    if fc <= 28:
        beta1 = 0.85
    elif fc >= 55:
        beta1 = 0.65
    else:
        beta1 = 0.85-0.05*(fc-28)/7
    
    roMax = gamma*beta1*fc/fy*eu/(eu+0.005)
    AsMax = roMax*b*d
    fiMmax = 0.9*AsMax*fy*(d-AsMax*fy/(2*gamma*fc*b))

    AsMin = max(fc**0.5/(4*fy)*b*d, 1.4*b*d/fy)

    if Mu<fiMmax:
        numerador = 0.9*d-(0.81*d**2 - 1.8*Mu/(gamma*fc*b))**0.5
        denomidaor = 0.9*fy/(gamma*fc*b)
        As = numerador/denomidaor

        texto[0]="Acero a tracción = "+str(round(As*1e4,2))+"[cm2]"
        texto[1]="Acero a compresión = 0 [cm2]"
        texto[2]="Acero mínimo a tracción = "+str(round(AsMin*1e4,2))+"[cm2]"
        texto[3]="La viga NO NECESITA acero a compresión"
    else:
        M2 = (Mu-fiMmax)/0.9
        As2 = M2/(fy*(d-dp))
        As = AsMax+As2
        Asp = As2
        roY = gamma*fc/fy*beta1*eu/(eu-fy/Es)*dp/d+Asp/(b*d)
        ro = As/(b*d)

        if ro>roY:
            texto[0]="Acero a tracción = "+str(round(As*1e4,2))+"[cm2]"
            texto[1]="Acero a compresión = "+str(round(Asp*1e4,2))+"[cm2]"
            texto[2]="Acero mínimo a tracción = "+str(round(AsMin*1e4,2))+"[cm2]"
            texto[3]="La viga NECESITA acero a compresión. As' fluye"
        else:
            a = (As-Asp)*fy/(gamma*fc*b)
            c = a/beta1
            fsp = eu*Es*(c-dp)/c
            AsRev = Asp*fy/fsp

            texto[0]="Acero a tracción = "+str(round(As*1e4,2))+"[cm2]"
            texto[1]="Acero a compresión = "+str(round(AsRev*1e4,2))+"[cm2]"
            texto[2]="Acero mínimo a tracción = "+str(round(AsMin*1e4,2))+"[cm2]"
            texto[3]="La viga NECESITA acero a compresión. As' no fluye"
    
    return texto