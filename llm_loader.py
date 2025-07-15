from llama_cpp import Llama

# Ruta al model GGUF (ajusta si cal)
MODEL_PATH = "./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Carrega el model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,            # Mida del context
    n_threads=6,           # Ajusta segons la teva CPU
    n_gpu_layers=0,        # Si tens GPU amb suport CUDA, pots pujar-ho (0 = només CPU)
    verbose=True
)

# Funció per fer preguntes
def pregunta_al_model(prompt: str) -> str:
    resposta = llm(
        prompt,
        max_tokens=512,
        stop=["</s>"],
        temperature=0.1,
        top_p=0.95
    )
    return resposta["choices"][0]["text"].strip()
