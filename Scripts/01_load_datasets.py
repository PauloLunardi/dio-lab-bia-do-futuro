# carregar o dataset
# Este script faz o carregamento inicial dos datasets usados no projeto Satoshi AI

from datasets import load_dataset


# Dataset principal: explicação geral sobre Bitcoin
bitcoin_dataset = load_dataset(
    "Gopher-Lab/bankless_DEBRIEF_-_What_is_Bitcoin"
)

# Dataset complementar: contexto histórico e influências de Satoshi Nakamoto e Vitalik Buterin
celestia_dataset = load_dataset(
    "Gopher-Lab/laurashin_How_Satoshi_Nakamoto_and_Vitalik_Buterin_Inspired_Key_Parts_of_Celestia_-_Ep__672"
)

# =========================
# SHA-256 experiments datasets


# Versão "bounded" do dataset de SHA-256 reduzido
sha256_bounded = load_dataset(
    "bshepp/round-reduced-sha256-learnability",
    "bounded_null"
)

# Versão dinâmica validada do SHA-256 reduzido
sha256_dynamics = load_dataset(
    "bshepp/round-reduced-sha256-learnability",
    "dynamics_validated"
)

# Dataset de análise de features (feature probing)
sha256_probe = load_dataset(
    "bshepp/round-reduced-sha256-learnability",
    "feature_probe"
)
