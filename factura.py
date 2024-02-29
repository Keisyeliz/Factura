import os
os.system('cls')
var_totalGFlt =0
cons_computadorInt = 1000000
cons_tabletasInt = 500000
cons_videobeamInt = 400000
cons_tvInt = 800000

var_nombreStr = input('Nombre del cliente -> ') 
var_contactoStr = input('Contacto del cliente -> ')
var_direccionStr = input('direccion del cliente -> ')
var_controlBln = True
while var_controlBln ==True:
    os.system('cls')
    print('cliente:  ',var_nombreStr)
    var_opcionStr = int(input('<<<MENÚ DE OPCIONE>>>\n\n1. computadores\n2. Tabletas\n3. videobeam\n4. tv\n5. Facturar\n -> '))
    if var_opcionStr >1 and var_opcionStr <=4:
        var_cantidadInt = int(input('cantidad ->'))
        
    if var_opcionStr == 1:
        var_totalGFlt += (var_cantidadInt * cons_computadorInt)
        
    if var_opcionStr == 2:
        var_totalGFlt += (var_cantidadInt * cons_tabletasInt)

    if var_opcionStr == 3:
        var_totalGFlt += (var_cantidadInt * cons_videobeamInt)

    if var_opcionStr == 4:
        var_totalGFlt += (var_cantidadInt * cons_tvInt)
        
    if var_opcionStr == 5:
            print('FACTURA')
            print('El total a pagar es $',var_totalGFlt)
            print('Gracias por su compra')
            var_controlBln = False