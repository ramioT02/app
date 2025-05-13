import React from 'react';


export default function Test(){
    return(
        <div class="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 p-6">
            <div class="card transform transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:bg-gray-100 hover:-rotate-1">
                <h2 class="card-title">Card Fantastica 1</h2>
                <p class="card-text">Questa card ha uno zoom, ombra potente e un piccolo tilt 3D!</p>
                <a href="#" class="card-button">Esplora</a>
            </div>

            <div class="card transform transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:bg-gray-100 hover:rotate-1">
                <h2 class="card-title">Card Fantastica 2</h2>
                <p class="card-text">Ogni card reagisce in modo dinamico al passaggio del mouse.</p>
                <a href="#" class="card-button">Scopri</a>
            </div>

            <div class="card transform transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:bg-gray-100 hover:-rotate-1">
                <h2 class="card-title">Card Fantastica 3</h2>
                <p class="card-text">Questo è il potere di Tailwind CSS + fantasia!</p>
                <a href="#" class="card-button">Prova ora</a>
            </div>
        </div>

    );
}
