# lmm_playground

My own playground to run local llm lmm etc.

Run with `llama.cpp`
 - Personal notes: https://gist.github.com/youliangtan/1f681ee822d497eef1f54ef5eb78c2bd

Running Llava
 - https://github.com/haotian-liu/LLaVA

Stable Diffusion:
 - https://www.assemblyai.com/blog/how-to-run-stable-diffusion-locally-to-generate-images/

Ollama
 - NOTE: Ollama uses llama.cpp under the hood
 - Model store: https://ollama.ai/library/
 - Run Mixtral
    - Default uses CPU, follow this: https://github.com/jmorganca/ollama/issues/1556#issuecomment-1859235636
    - use: `ollama create mixtral_gpu -f ./Mixtral_Modelfile` to create a new model
