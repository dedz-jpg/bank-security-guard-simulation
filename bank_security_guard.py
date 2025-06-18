# Simulação de Segurança de Banco - Bank Security Guard

# Simulação de horário (para exemplo)
horario_atual = 17  # Simulando como se fossem 17 horas (antes das 18h)

# Simulação de clientes do lado de fora
clientes_fora = ["Cliente 1", "Cliente 2", "Cliente 3"]

# Fila de atendimento
fila = []

# Enquanto o horário for antes das 18h
while horario_atual < 18:
    print(f"Horário atual: {horario_atual}h")

    if clientes_fora:
        cliente = clientes_fora.pop(0)
        fila.append(cliente)
        print(f"{cliente} adicionado à fila de atendimento.")
    else:
        print("Nenhum cliente aguardando do lado de fora.")

    # Simulação de passagem de tempo (incrementando 1 hora por iteração)
    horario_atual += 1

print("São 18h. Banco fechado pelo segurança.")
