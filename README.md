🎨 AI Image Generator Using Stable Diffusion

An AI-powered web application that generates high-quality images from natural language text prompts using Stable Diffusion v1.5 and Hugging Face Diffusers. The application is built with Python and Streamlit, providing a clean and interactive interface for real-time AI image generation.

🚀 Project Overview

This project was developed as part of the Prodigy InfoTech Generative AI Internship (Task 2). It demonstrates the capabilities of Generative AI by converting user text prompts into realistic, high-quality images using the Stable Diffusion v1.5 model. The application offers an intuitive web interface for generating and downloading AI-created images.

✨ Features

* 🖼️ Generate images from text prompts
* 🤖 Powered by Stable Diffusion v1.5
* ⚡ Fast AI image generation
* 🎨 Clean and user-friendly Streamlit interface
* 📥 Download generated images
* 💻 Supports both CPU and GPU execution
* 🐳 Docker support for easy deployment
* 📂 Simple project structure

🛠️ Technology Stack

* Python
* Streamlit
* Hugging Face Diffusers
* Stable Diffusion v1.5
* PyTorch
* Pillow (PIL)
* Docker
* Git & GitHub

📂 Project Structure

PRODIGY_GA_02/
│── .streamlit/
│── assets/
│── app.py
│── requirements.txt
│── Dockerfile
│── .gitignore
│── .dockerignore
│── README.md

⚙️ Installation

Clone the Repository

git clone https://github.com/Saikishorep15/PRODIGY_GA_02.git
cd PRODIGY_GA_02

Create a Virtual Environment

python -m venv .venv

Activate the Virtual Environment

Windows

.venv\Scripts\activate

Linux / macOS

source .venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Run the Application

streamlit run app.py

🎯 Usage

1. Launch the Streamlit application.
2. Enter a descriptive text prompt.
3. Click Generate Image.
4. Wait for the AI model to generate the image.
5. Preview and download the generated image.

📸 Sample Prompt

A futuristic cyberpunk city at night with neon lights and flying cars.

📦 Model Used

* Stable Diffusion v1.5
* Hugging Face Diffusers
* PyTorch Backend

🐳 Docker

Build the Docker Image

docker build -t ai-image-generator .

Run the Docker Container

docker run -p 8501:8501 ai-image-generator

📚 Learning Outcomes

* Text-to-Image Generation
* Stable Diffusion Architecture
* Hugging Face Diffusers
* Streamlit Web Application Development
* Generative AI Deployment
* Docker Containerization
* Git & GitHub Version Control

👨‍💻 Developer

Priyanka R

Information Science and Engineering Student

Jain Institute of Technology, Davangere

GitHub: https://github.com/priyapriyanka29

Repository: https://github.com/priyapriyanka29/PRODIGY_GA_02

📄 License

This project was developed for learning and educational purposes as part of the Prodigy InfoTech Generative AI Internship (Task 2).





