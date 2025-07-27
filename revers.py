import gradio as gr

def reverse_text(text):
    return text[::-1]

with gr.Blocks(theme="soft") as app:
    gr.Markdown("## 🔤 Sentence Reverser")
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input Sentence", placeholder="Type here...")
            btn = gr.Button("Reverse", variant="primary")
        with gr.Column():
            output_text = gr.Textbox(label="Reversed", interactive=False)
    
    btn.click(fn=reverse_text, inputs=input_text, outputs=output_text)
    gr.Examples(
        examples=["Hello world", "Gradio is awesome", "Python programming"],
        inputs=input_text
    )

app.launch()