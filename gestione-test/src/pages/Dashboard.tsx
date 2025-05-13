import React from 'react';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

interface User {
  nome: string;
  cognome: string;
  email: string;
}

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:8000/api/me", {
      method: "GET",
      credentials: "include"
    })
      .then(res => {
        if (!res.ok) throw new Error("Non autenticato");
        return res.json();
      })
      .then(data => setUser(data))
      .catch(() => {
        // Se il token è assente o invalido → torna al login
        navigate("/login");
      });
  }, [navigate]);

  const handleLogout = async () => {
    await fetch("http://localhost:8000/api/logout", {
      method: "POST",
      credentials: "include",
    });

    navigate("/login");
  };


  return (
    <div className="p-6 text-center">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      {user ? (
        <>
          <p>Benvenuto, <strong>{user.nome} {user.cognome}</strong></p>
          <p>Email: {user.email}</p>

          <button
            onClick={handleLogout}
            className="mt-6 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
          >
            Logout
          </button>
          
        </>
      ) : (
        <p>Caricamento dati utente...</p>
      )}
    </div>
  );
}
