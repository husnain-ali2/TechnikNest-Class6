import gradio as gr
# Use one of these proper theme names:
gr.Interface(
    lambda x: x*x,
    gr.Number(),
    "number",
    
).launch()