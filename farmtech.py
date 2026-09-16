# ==========================================
# REQUISITO D: Dados organizados em vetores
# ==========================================
vetor_culturas = []
vetor_areas = []
vetor_insumos = []

# ==========================================
# REQUISITO F: Rotinas de loop e decisão
# ==========================================
while True:
    print("\n" + "=" * 40)
    print("🌾 FARMTECH SOLUTIONS 🌾")
    print("=" * 40)
    # REQUISITO E: Menu de opções exato
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualização de dados")
    print("4. Deleção de dados")
    print("5. Sair do programa")
    print("=" * 40)

    opcao = input("Escolha uma opção (1-5): ")

    # ------------------------------------------
    # 1. ENTRADA DE DADOS
    # ------------------------------------------
    if opcao == '1':
        print("\n--- ENTRADA DE DADOS ---")

        # REQUISITO A: Suporte a 2 tipos de culturas
        cultura = input("Digite a cultura (Cana ou Café): ").strip().capitalize()

        if cultura == "Cana" or cultura == "Café":
            # REQUISITO B: Cálculo de área (Retângulo)
            print("\n-- Cálculo de Área (Retângulo) --")
            base = float(input("Digite a base da lavoura em metros: "))
            altura = float(input("Digite a altura da lavoura em metros: "))
            area_total = base * altura

            # REQUISITO C: Cálculo do manejo de insumos (Exemplo do PDF)
            print("\n-- Cálculo de Insumos --")
            print("Lógica: Pulverizar 500 mL (0.5 Litros) por metro.")
            produto = "Fosfato Líquido" if cultura == "Café" else "Fertilizante Líquido"

            qtd_ruas = int(input("Quantas ruas a lavoura tem? "))
            comp_rua = float(input("Qual o comprimento de cada rua em metros? "))

            # Cálculo: (Quantidade de ruas * Comprimento da rua) * 0.5 Litros
            litros_necessarios = (qtd_ruas * comp_rua) * 0.5

            # Salvando nos vetores
            vetor_culturas.append(cultura)
            vetor_areas.append(area_total)
            vetor_insumos.append(litros_necessarios)

            posicao = len(vetor_culturas) - 1
            print(f"\n✅ Cadastro realizado na POSIÇÃO [{posicao}] do vetor.")
            print(f"Área: {area_total} m² | Produto: {produto} | Total: {litros_necessarios} Litros.")
        else:
            print("❌ Cultura inválida! Escolha apenas Cana ou Café.")

    # ------------------------------------------
    # 2. SAÍDA DE DADOS
    # ------------------------------------------
    elif opcao == '2':
        print("\n--- SAÍDA DE DADOS ---")
        if len(vetor_culturas) == 0:
            print("O vetor está vazio.")
        else:
            for i in range(len(vetor_culturas)):
                print(
                    f"Posição [{i}] | Cultura: {vetor_culturas[i]} | Área: {vetor_areas[i]} m² | Insumo: {vetor_insumos[i]} Litros")

    # ------------------------------------------
    # 3. ATUALIZAÇÃO DE DADOS
    # ------------------------------------------
    elif opcao == '3':
        print("\n--- ATUALIZAÇÃO DE DADOS ---")
        posicao = int(input("Digite a POSIÇÃO do vetor que deseja atualizar (ex: 0, 1): "))

        # Verifica se a posição existe no vetor
        if 0 <= posicao < len(vetor_culturas):
            print(f"Atualizando dados da cultura: {vetor_culturas[posicao]}")

            # Novos cálculos para atualizar
            nova_base = float(input("Digite a nova base em metros: "))
            nova_altura = float(input("Digite a nova altura em metros: "))
            nova_area = nova_base * nova_altura

            novas_ruas = int(input("Quantas ruas a lavoura tem agora? "))
            novo_comp = float(input("Qual o novo comprimento de cada rua? "))
            novo_insumo = (novas_ruas * novo_comp) * 0.5

            # Substituindo os valores antigos na posição
            vetor_areas[posicao] = nova_area
            vetor_insumos[posicao] = novo_insumo

            print("✅ Dados atualizados com sucesso!")
        else:
            print("❌ Posição não encontrada no vetor.")

    # ------------------------------------------
    # 4. DELEÇÃO DE DADOS
    # ------------------------------------------
    elif opcao == '4':
        print("\n--- DELEÇÃO DE DADOS ---")
        posicao = int(input("Digite a POSIÇÃO do vetor que deseja deletar: "))

        if 0 <= posicao < len(vetor_culturas):
            vetor_culturas.pop(posicao)
            vetor_areas.pop(posicao)
            vetor_insumos.pop(posicao)
            print("✅ Dados deletados com sucesso!")
        else:
            print("❌ Posição não encontrada no vetor.")

    # ------------------------------------------
    # 5. SAIR DO PROGRAMA
    # ------------------------------------------
    elif opcao == '5':
        print("\nEncerrando o sistema FarmTech Solutions...")
        break

    else:
        print("\n❌ Opção inválida. Escolha um número de 1 a 5.")