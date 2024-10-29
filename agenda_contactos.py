
def mostrar_menu():
    print('\nAgenda de contactos:\n')
    print('1. Agregar nuevo contacto\n ')
    print('2. Eliminar contacto existente\n')
    print('3. Buscar contacto\n')
    print('4. Lista de contactos\n')
    print('5. Salir del programa\n ')
    print('\n')

def agregar_contacto(agenda):
    nombre = input('Por favor introduzca el nombre completo del contacto: ')
    telefono = input('Por favor introduzca el teléfono del contacto: ')
    email = input('Por favor introduzca el email del contacto: ')
    agenda[nombre] = { 'telefono': telefono, 'email': email}
    print(f'\n!Se ha agregado el contacto {nombre} exitosamente! ')

def eliminar_contacto(agenda):
    nombre = input('\nIngrese el nombre de la agenda que desea eliminar: ')
    if nombre in agenda:
        del agenda[nombre]
        print(f'\nEl contacto de {nombre} ha sido eliminado correctamente. ')
    else:
        print(f'\nNo se ha encontrado un contacto con el nombre {nombre}')

def buscar_contacto(agenda):
    nombre =input('Ingrese el nombre del contacto que está buscando: ')
    if nombre in agenda:
        print(f'Nombre: {nombre}')
        print(f'Teléfono: {agenda[nombre]['telefono']}')
        print(f'Email: {agenda[nombre]['email']}')
    else:
        print(f'El contacto {nombre} no ha sido encontrado en la agenda')

def listar_contactos(agenda):
    if agenda:
        print('\nLista de contactos: ')
        
        for nombre, info in agenda.items():
            print(f'\nNombre: {nombre}')
            print(f'Teléfono: {info['telefono']}')
            print(f'Email: {info['email']}')
            print('-' * 20)
    else:
        print('\nLa agenda aún está vacía')


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input('Por favor elija una opción: ')
        print('')

        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            listar_contactos(agenda)
        elif opcion == '5':
            print('Usted ha salido de la agenda de contactos')
            break
        else:
            print('Por favor seleccione una opción valida (del 1 al 5)')

agenda_contactos()