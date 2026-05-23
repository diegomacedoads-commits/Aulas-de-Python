# Controle de despesas mensais

salario = float(input("Digite o seu salário mensal: R$ "))

despesas = {}
total_despesas = 0

while True:
    descricao = input(
        "\nDigite a descrição da despesa (ou 'sair' para encerrar): "
    )

    if descricao.lower() == "sair":
        break

    valor = float(input(f"Digite o valor da despesa '{descricao}': R$ "))

    despesas[descricao] = valor
    total_despesas += valor

saldo = salario - total_despesas

print("\n===== RESUMO FINANCEIRO =====")
print(f"Salário mensal: R$ {salario:.2f}")

print("\nDespesas:")
for descricao, valor in despesas.items():
    print(f"- {descricao}: R$ {valor:.2f}")

print(f"\nTotal de despesas: R$ {total_despesas:.2f}")
print(f"Saldo restante: R$ {saldo:.2f}")

if saldo > 0:
    print("Você conseguiu economizar este mês!")
elif saldo == 0:
    print("Você gastou exatamente o valor do salário.")
else:
    print("Atenção! Você gastou mais do que ganhou.")
