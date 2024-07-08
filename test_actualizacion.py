from actualizacion_perfil import Cliente

def test_actualizacion_perfil_exitosa():
    cliente = Cliente("Juan", "Pérez García", "juan@example.com", "contraseña123", "12345678X", 30)
    resultado = cliente.actualizar_perfil()
    assert resultado == True
