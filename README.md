<!-- GETTING STARTED -->
## Getting Started

This is a sample project that integrates different tools and libraries for front-end work and Django for the back-end.

### Prerequisites

This example requires the following tools to be installed in the development environment:
* node ~= 22.10.0
* python3
* python3-pip

### Installation

_Perform the following steps after you have prepared your development environment:_

1. Clone the repo
   ```sh
   git clone https://github.com/jsolorzano/django-vite-demo.git
   ```
2. Move to the generated folder
   ```sh
   cd django-vite-demo
   ```
3. Install django and django-vite
   ```sh
   pip install -r requirements.txt
   ```
4. Create the database tables
   ```sh
   python manage.py migrate
   ```
5. Install NPM packages
   ```sh
   npm install
   ```

<!-- USAGE -->
## Usage

To launch the application, execute the following instructions:

1. Open a terminal and activate the front-end development and debugging tool
   ```sh
   npm run dev
   ```
2. Open a terminal and activate the Django development server
   ```sh
   python mange.py runserver
   ```
3. Navigate to URL enabled by your development server, for example: http://localhost:8000/