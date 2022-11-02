altura= float (input(" qual é a sua altura em cm: "))
peso= float (input(" qual é o seu peso em kg: "))

IMC  = peso/(altura/100)** 2
print(IMC)

if IMC < 18.5:
    print("f seu IMC é de {IMC}   é classificado como magreza")
    
elif IMC>=18.5 and IMC <  24.9: 
    print("f seu IMC é de {IMC}   é classificado como normal")
elif IMC>=25 and IMC <  29.9: 
    print("f seu IMC é de {IMC}   é classificado como sobrepeso , mas bem pouco não se preocupe")
elif IMC>=30 and IMC <  100: 
    print("f seu IMC é de {IMC}  é classificado como obesidade")
    
    
    