import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
import io


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)


# =====================================
# CUSTOM CSS DESIGN
# =====================================

st.markdown(
"""
<style>

.stApp {
    background-color:#0e1117;
    color:white;
}

.main-title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#00FFFF;
}

.sub-title {
    text-align:center;
    color:#AAAAAA;
    font-size:18px;
}


.stButton button {

    background-color:#00FFFF;
    color:black;
    border-radius:12px;
    height:50px;
    width:100%;
    font-weight:bold;

}

</style>
""",
unsafe_allow_html=True
)



# =====================================
# HEADER
# =====================================


st.markdown(
"""
<div class="main-title">
🎨 AI Image Generator Using Stable Diffusion
</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="sub-title">
Generate AI Images from Text Prompts using 
Stable Diffusion and Hugging Face Diffusers
</div>
""",
unsafe_allow_html=True
)


st.divider()



# =====================================
# SIDEBAR
# =====================================


with st.sidebar:

    st.title("🤖 AI Model Info")


    st.write("Model")

    st.success(
        "Stable Diffusion"
    )


    st.write("Framework")

    st.info(
        "Hugging Face Diffusers"
    )


    st.write("Backend")

    st.warning(
        "PyTorch"
    )


    st.write("Developer")

    st.success(
        "SaiKishore P"
    )




# =====================================
# LOAD AI MODEL
# =====================================


@st.cache_resource
def load_model():


    device = (
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )


    model_id = "segmind/tiny-sd"



    pipe = StableDiffusionPipeline.from_pretrained(

        model_id,

        torch_dtype=torch.float32,

        safety_checker=None

    )


    pipe.to(device)


    pipe.enable_attention_slicing()


    return pipe




with st.spinner(
    "Loading AI Model..."
):

    pipe = load_model()




# =====================================
# USER INPUT
# =====================================


prompt = st.text_area(

    "Enter your image prompt:",

    placeholder=
    "Example: A cyberpunk city at night"

)



generate = st.button(
    "Generate Image 🚀"
)




# =====================================
# GENERATE IMAGE
# =====================================


if generate:


    if prompt.strip() == "":


        st.warning(
            "Please enter a prompt"
        )


    else:


        try:


            with st.spinner(
                "Generating AI Image..."
            ):


                image = pipe(

                    prompt,

                    height=256,

                    width=256,

                    num_inference_steps=15

                ).images[0]



            st.success(
                "Image Generated Successfully 🎉"
            )



            st.image(

             image,

             caption=prompt,

              width=300

            )


            buffer = io.BytesIO()


            image.save(

                buffer,

                format="PNG"

            )



            st.download_button(

                label="Download Image",

                data=buffer.getvalue(),

                file_name="ai_generated_image.png",

                mime="image/png"

            )




        except Exception as error:


            st.error(
                "Generation Failed"
            )


            st.write(error)