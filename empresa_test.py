# -*- coding: utf-8 -*-
from empresa import Empresa, Estagiario, Programador, Vendedor

# ------------------------ Programador -------------------------------
def test_prog_cg_invalida():
    try:
        Programador('Fulano', 25, 'fulano@empresa.com', 15)
        Programador('Fulano', 25, 'fulano@empresa.com', 42)
    except ValueError:
        pass
    else:
        raise AssertionError('Programador criado com carga horária inválida')


def test_prog_consulta_cg():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    msg = ('o método consulta_carga_horária não retornou o valor da '
           'carga horaria semanal')
    assert prog.consulta_carga_horaria() == 40, msg


def test_prog_altera_cg():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    prog.altera_carga_horaria(36)
    msg = 'A carga horária não foi alterada para o novo valor'
    assert prog.consulta_carga_horaria() == 36, msg


def test_prog_altera_cg_error():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    try:
        prog.altera_carga_horaria(16)
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert prog.consulta_carga_horaria() == 40, msg
    else:
        raise AssertionError('Não levantou um ValueError para carga inválida')


def test_prog_calcula_salario():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    msg = 'Salário do programador calculado incorretamente'
    assert prog.calcula_salario() == 6300, msg


def test_prog_recebe_aumento():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    prog.aumenta_salario()
    msg = 'Aumento do salário de programador calculado incorretamente'
    assert prog.calcula_salario() == 6615, msg


# ------------------- Estagiário -----------------------------
def test_est_cg_invalida():
    try:
        Estagiario('Fulano', 25, 'fulano@empresa.com', 10)
        Estagiario('Fulano', 25, 'fulano@empresa.com', 35)
    except ValueError:
        pass
    else:
        raise AssertionError('Estagiário criado com carga horária inválida')


def test_est_consulta_cg():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    msg = ('o método consulta_carga_horária não retornou o valor da '
           'carga horaria semanal')
    assert est.consulta_carga_horaria() == 20, msg


def test_est_altera_cg():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    est.altera_carga_horaria(30)
    msg = 'A carga horária não foi alterada para o novo valor'
    assert est.consulta_carga_horaria() == 30, msg


def test_est_altera_cg_error():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    try:
        est.altera_carga_horaria(36)
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert est.consulta_carga_horaria() == 20, msg
    else:
        raise AssertionError('Não levantou um ValueError para carga inválida')


def test_est_calcula_salario():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'Salário do estagiário calculado incorretamente'
    assert est.calcula_salario() == 1645, msg


def test_est_recebe_aumento():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    est.aumenta_salario()
    msg = 'Aumento do salário do estagiário calculado incorretamente'
    assert abs(est.calcula_salario() - 1714.75) < 0.01, msg


# ------------------- Vendedor -----------------------------
def test_vend_cg_invalida():
    try:
        Vendedor('Fulano', 20, 'fulano@empresa.com', 10)
        Vendedor('Fulano', 20, 'fulano@empresa.com', 50)
    except ValueError:
        pass
    else:
        raise AssertionError('Vendedor criado com carga horária inválida')


def test_vend_consulta_cg():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = ('o método consulta_carga_horária não retornou o valor da '
           'carga horaria semanal')
    assert vend.consulta_carga_horaria() == 20, msg


def test_vend_altera_cg():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.altera_carga_horaria(45)
    msg = 'A carga horária não foi alterada para o novo valor'
    assert vend.consulta_carga_horaria() == 45, msg


def test_vend_altera_cg_error():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    try:
        vend.altera_carga_horaria(46)
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert vend.consulta_carga_horaria() == 20, msg
    else:
        raise AssertionError('Não levantou um ValueError para carga inválida')


def test_vend_consulta_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'O número de visitas deve ser iniciado em zero'
    assert vend.consulta_visitas() == 0, msg


def test_vend_realizar_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.realizar_visita(3)
    msg = 'Não atualizou o número de visitas do vendedor corretamente'
    assert vend.consulta_visitas() == 3, msg
    vend.realizar_visita(6)
    assert vend.consulta_visitas() == 9, msg


def test_vend_realizar_visitas_error():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    testes = ['5', 'abc', 5.2, -3, 0]
    for teste in testes:
        try:
            vend.realizar_visita(teste)
        except TypeError:
            assert not isinstance(teste, int), 'Levantou TypeError para entrada inteira'
        except ValueError:
            assert isinstance(teste, int), 'Levantou ValueError para entrada que não é inteira'
            assert teste <= 0, 'Levantou ValueError para entrada válida'
        except Exception:
            raise AssertionError('Não levantou o erro do tipo pedido')
        else:
            raise AssertionError('Não levantou nenhum erro para uma entrada inválida')


def test_vend_zerar_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.realizar_visita(5)
    vend.zerar_visitas()
    msg = 'O número de visitas não foi zerado corretamente'
    assert vend.consulta_visitas() == 0, msg


def test_vend_calcula_salario01():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'Salário do vendedor calculado incorretamente'
    assert vend.calcula_salario() == 3050.0, msg


def test_vend_calcula_salario02():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.realizar_visita(23)
    msg = 'Salário do vendedor calculado incorretamente'
    assert vend.calcula_salario() == 3740.0, msg


def test_vend_recebe_aumento():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.aumenta_salario()
    msg = 'Aumento do salário do vendedor calculado incorretamente'
    assert abs(vend.calcula_salario() - 3185.0) < 0.01, msg


# ----------------- Empresa ---------------------------------
def test_01_lista_func_empresa():
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    assert emp.lista_fucionarios() == [], 'A lista de funcionários deve começar com o valor passado'


def test_02_comeca_func_empresa():
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [est])
    assert len(emp.lista_fucionarios()) == 1, 'A lista de funcionários dever começar com o valor passado'
    assert emp.lista_fucionarios()[0].nome == 'Pedro', 'O funcionário não foi adicionado à lista'


def test_03_inclui_func():
    est = Estagiario('Maria', 25, 'maria@empresa.com', 20)
    prog = Programador('Ana', 31, 'ana@empresa.com', 40)
    vend = Vendedor('Marcos', 28, 'marcos@empresa.com', 35)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(est)
    emp.contrata(prog)
    emp.contrata(vend)
    funcinarios = emp.lista_fucionarios()
    assert len(funcinarios) == 3, 'Lista de funcionários não contém o número correto de funcionários contratados'
    assert funcinarios[0].nome == 'Maria', 'O primeiro item da lista não é o primeiro funcionário contratado'
    assert funcinarios[1].nome == 'Ana', 'O segundo item da lista não é o segundo funcionário contratado'
    assert funcinarios[2].nome == 'Marcos', 'O terceiro item da lista não é o terceiro funcionário contratado'


def test_04_folha_pagamento():
    prog = Programador('Julia', 31, 'julia@empresa.com', 40)
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    vend1 = Vendedor('Mauro', 41, 'mauro@empresa.com', 35)
    vend2 = Vendedor('Carla', 36, 'carla@empresa.com', 45)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(prog)
    emp.contrata(est)
    emp.contrata(vend1)
    emp.contrata(vend2)
    vend1.realizar_visita(7)
    vend2.realizar_visita(10)
    assert emp.folha_pagamento() == 19955.0, 'Folha de pagamento calculada errada'
# ---------------------------------------------------------------
