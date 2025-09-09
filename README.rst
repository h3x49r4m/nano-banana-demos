###############################################################################
Nano Banana Demos
###############################################################################

Nano Banana Demos is a versatile project showcasing the capabilities of Google's Gemini API,
with a primary focus on image generation and manipulation based on text prompts and input images.
It provides both a command-line interface (CLI) for direct interaction and a web application
for a more interactive user experience.

Features
--------

*   **Image Generation:** Generate new images based on textual prompts and an initial image input.
*   **CLI Interface:** Interact with the Gemini API directly from your terminal for quick experiments.
*   **Web Application:** A user-friendly web interface for real-time image generation and visualization.
*   **Gemini Integration:** Leverages the Google Gemini API for advanced generative AI functionalities.

Installation
------------

To set up the project, follow these steps:

1.  **Clone the repository:**

    .. code-block:: bash

        git clone https://github.com/h3x49r4m/nano_banana_demos.git
        cd nano_banana_demos

2.  **Set up Python environment (for CLI and Backend):**

    It's recommended to use a virtual environment.

    .. code-block:: bash

        python3 -m venv .venv
        source .venv/bin/activate
        pip install -e .

    This will install all necessary Python dependencies, including those for the CLI and the FastAPI backend.

3.  **Set up Node.js environment (for Frontend):**

    Navigate to the `webapp/frontend` directory and install Node.js dependencies.

    .. code-block:: bash

        cd webapp/frontend
        npm install
        cd ../..

4.  **Configure Gemini API Key:**

    Create a `.env` file in the root directory of the project and add your Gemini API key:

    .. code-block:: ini

        GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

    Replace ``YOUR_GEMINI_API_KEY`` with your actual API key.

Usage
-----

### Command-Line Interface (CLI)

You can use the CLI to generate images from a prompt file.

1.  **Activate your Python virtual environment:**

    .. code-block:: bash

        source .venv/bin/activate

2.  **Run the CLI with a prompt file:**

    .. code-block:: bash

        python cli/main.py --prompt prompts/infographics/activation_functions/activations_prompt.txt

    You can use any of the prompt files located in the `prompts/` directory.

### Web Application

The web application provides an interactive way to generate images.

1.  **Start the Backend Server:**

    First, activate your Python virtual environment.

    .. code-block:: bash

        source .venv/bin/activate
        uvicorn webapp.backend.server:app --host 0.0.0.0 --port 8000 --reload

    The backend server will start on `http://localhost:8000`.

2.  **Start the Frontend Development Server:**

    In a new terminal, navigate to the frontend directory.

    .. code-block:: bash

        cd webapp/frontend
        npm start

    The frontend application will typically open in your browser at `http://localhost:3000`.

    Now you can enter prompts in the web interface and see the generated images.

Project Structure
-----------------

::

    .
    ├── cli/                     # Command-Line Interface application
    │   ├── gemini_client.py     # Gemini API client for CLI
    │   └── main.py              # Main CLI entry point
    ├── docs/                    # Project documentation
    ├── prompts/                 # Collection of prompt files for various demos
    │   ├── design/
    │   └── infographics/
    ├── webapp/                  # Web application
    │   ├── backend/             # FastAPI backend
    │   │   ├── gemini_client.py # Gemini API client for backend
    │   │   └── server.py        # FastAPI server
    │   ├── frontend/            # React frontend
    │   │   ├── public/
    │   │   └── src/             # React source code
    │   └── static/              # Static files served by the backend (e.g., generated images)
    ├── .gitignore
    ├── pyproject.toml           # Project metadata and Python dependencies
    └── README.rst               # This README file

Prompt Categories
-----------------

The `prompts/` directory contains a diverse collection of prompt files, organized into categories to demonstrate various capabilities of the Gemini API.

*   **`prompts/design/`**: Contains prompts related to general design tasks, focusing on visual composition and specific design elements.
    *   Example: Creating a blank music sheet.

*   **`prompts/infographics/`**: Contains highly structured prompts for generating educational and scientific infographics, detailing visual layouts and illustrative elements for complex topics.
    *   Subcategories include: Activation Functions, Dark Matter & Dark Energy, Dynamic Systems, and Earth Science.

*   **`prompts/templates/`**: This extensive collection showcases a wide range of image generation and manipulation tasks, further categorized for clarity:
    *   **`Artistic_Transformations`**: Prompts for transforming images into different artistic styles (e.g., classic painting, Lego, sculpture, stickers, minimalist negative space).
    *   **`Character_Design_Art`**: Prompts focused on character creation, design, poses, and transforming illustrations or anime into different forms.
    *   **`Image_Editing_Analysis`**: Prompts for tasks like image annotation, enhancement, restoration, and applying specific visual modifications (e.g., changing hairstyles).
    *   **`Infographics_Content`**: Prompts for generating infographics and images that incorporate text for informational purposes.
    *   **`Object_3D_Visualization`**: Prompts for creating 3D models from photos, generating multi-view representations of objects, and exploded views.
    *   **`Perspective_Spatial`**: Prompts that involve changing perspectives, generating cross-sectional views, or adding augmented reality information to images.
    *   **`Photography_Scene_Generation`**: Prompts for creating realistic photographic scenes, product mockups, product packaging designs, and combining multiple image elements into a single scene.
    *   **`Scientific_Educational`**: Prompts for generating visual solutions to math puzzles or creating annotated models for academic/scientific presentations.
    *   **`Storytelling_Sequence`**: Prompts for generating sequential images or storyboards to tell a narrative.

Technologies Used
-----------------

*   **Python:**
    *   **FastAPI:** Web framework for the backend.
    *   **Google GenAI:** Python client library for the Gemini API.
    *   **Pillow:** Image processing library.
    *   **Uvicorn:** ASGI server for FastAPI.
*   **JavaScript/TypeScript:**
    *   **React:** Frontend library for building user interfaces.
    *   **Node.js/npm:** JavaScript runtime and package manager for the frontend.
