# ==========================================
# FASE 1: DADOS ESTATÍSTICOS (Exigência 'G')
# ==========================================
# Simulando os dados que foram gerados no sistema em Python
# (Você pode explicar no vídeo que esses vetores representam os dados salvos)
vetor_areas <- c(15000, 20000, 12000, 30000)
vetor_insumos <- c(750, 1000, 600, 1500) 

cat("========================================\n")
cat("📊 RELATÓRIO ESTATÍSTICO - FARMTECH 📊\n")
cat("========================================\n\n")

# Calculando a Média (mean) e Desvio Padrão (sd) para as Áreas
media_area <- mean(vetor_areas)
desvio_area <- sd(vetor_areas)

# Calculando a Média (mean) e Desvio Padrão (sd) para os Insumos
media_insumos <- mean(vetor_insumos)
desvio_insumos <- sd(vetor_insumos)

# Exibindo os resultados estatísticos no terminal
cat("--- DADOS DE ÁREA (m²) ---\n")
cat("Média das áreas plantadas:", media_area, "m²\n")
cat("Desvio Padrão das áreas:", round(desvio_area, 2), "m²\n\n")

cat("--- DADOS DE INSUMOS (Litros) ---\n")
cat("Média de insumos aplicados:", media_insumos, "Litros\n")
cat("Desvio Padrão de insumos:", round(desvio_insumos, 2), "Litros\n\n")


# ==========================================
# FASE 2: IR ALÉM - CONEXÃO COM API (Clima)
# ==========================================
# Carregando as bibliotecas necessárias para requisições web
library(httr)
library(jsonlite)

cat("========================================\n")
cat("🌤️  CONDIÇÕES METEOROLÓGICAS (API) 🌤️\n")
cat("========================================\n")

# URL da API pública Open-Meteo (Usando coordenadas gerais de São Paulo)
url_api <- "https://api.open-meteo.com/v1/forecast?latitude=-23.5489&longitude=-46.6388&current_weather=true"

# Fazendo a requisição (coleta de dados climáticos)
resposta <- GET(url_api)

# Verificando se a conexão deu certo (Código 200 significa sucesso)
if (status_code(resposta) == 200) {
  
  # Processando as informações recebidas (de JSON para texto em R)
  dados_clima <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  
  # Separando apenas a temperatura e a velocidade do vento
  temperatura_atual <- dados_clima$current_weather$temperature
  vento_atual <- dados_clima$current_weather$windspeed
  
  # Exibindo via texto simples no terminal
  cat("Conexão com API estabelecida com sucesso!\n")
  cat("Temperatura Atual na Região:", temperatura_atual, "°C\n")
  cat("Velocidade do Vento:", vento_atual, "km/h\n")
  
} else {
  cat("Erro ao conectar com a API Meteorológica.\n")
}
