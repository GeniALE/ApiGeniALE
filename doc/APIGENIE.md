# GeniALE Brewery API Documentation

## Introduction

Documentation de l'API REST permettant de gérer les membres, génies, départements, bières, photos, marchandises et événements.

---

## Table des matières

1. [Présentation](#présentation)
2. [Authentification](#authentification)
3. [Schémas](#schémas)
4. [Endpoints](#endpoints)

   * [GeniALE](#geniale)
   * [Membres](#membres)
   * [Départements](#départements)
   * [Exécutifs](#exécutifs)
   * [Bières](#bières)
   * [Notations](#notations)
   * [Photos](#photos)
   * [Marchandises](#marchandises)
   * [Événements](#événements)

---

## Présentation

Cette API permet de :

* Gérer les membres de géniale 
* Gérer les génies (personnes référencées)
* Gérer les départements
* Gérer les membres de l’exécutif
* Gérer les bières produites
* Gérer les photos (upload, téléchargement)
* Gérer la marchandise
* Gérer les événements, participants et photos liées

---

## Authentification
A discuter mais on reflechira a un systeme de token et d'auth peux etre 

---

## Schémas

Cette section regroupe les structures JSON utilisées par les routes.

### GeniALE

```json
{
  "id_geniALE": 42,
  "nom": "Dupont",
  "prenom": "Jean",
  "linkedin": "https://...",
  "photo_id": 12
}
```

### Membre

```json
{
  "id_membre": 1,
  "id_geniALE": 42,
  "id_departement": 3,
  "date_admission": "2024-09-01"
}
```

### Departement

```json
{
  "id_departement": 3,
  "nom": "Communication",
  "description": "Gestion des réseaux"
}
```

### Executif

```json
{
  "id_executif": 1,
  "id_geniALE": 42,
  "id_departement": 3,
  "poste": "Président",
  "description": "Responsable de l'équipe"
}
```

### NosBieres

```json
{
  "id_nosBiere": 1,
  "id_photo": 12,
  "nom": "Triple IPA",
  "description": "Une bière amère et riche",
  "date_date_production": "2025-03-01"
}
```

### NotationBiere

```json
{
  "id_notation": 1,
  "id_nosBiere": 2,
  "id_membre": 7,
  "note": 4.5
}
```

### Photo

```json
{
  "id_photo": 10,
  "nom": "img001.jpg",
  "taille": 204800,
  "type": "image/jpeg"
}
```

### Marchandise

```json
{
  "id_marchandise": 1,
  "id_photo": 10,
  "nom": "T-shirt",
  "description": "T-shirt officiel",
  "prix": 15.0
}
```

### Evenement

```json
{
  "id_evenement": 1,
  "nom": "Soirée dégustation",
  "description": "Découverte des nouvelles bières",
  "date_event": "2025-06-11"
}
```

---

## Endpoints

Cette section décrit toutes les routes de l’API.

---

## GeniALE

### GET /geniale

Liste tous les membres .

### POST /geniale

Crée un nouveau membre (auth requis).

### GET /geniale/{id}

Récupère un membre.

### PUT /geniale/{id}

Modifie un membre (auth requis).

### DELETE /geniale/{id}

Supprime un membre (auth requis).

---

## Membres

### GET /membres

Liste tous les membres.

### POST /membres

Crée un membre.

### GET /membres/{id}

Récupère un membre.

### PUT /membres/{id}

Modifie un membre.

### DELETE /membres/{id}

Supprime un membre.

---

## Départements

### GET /departements

Liste des départements.

### POST /departements

Crée un département.

---

## Exécutifs

### GET /executifs

Liste les exécutifs.

### POST /executifs

Crée un exécutif.

---

## Bières

### GET /nosbieres

Liste toutes les bières.

### POST /nosbieres

Crée une bière.

### GET /nosbieres/{id}

Récupère une bière.

### PUT /nosbieres/{id}

Met à jour une bière.

### DELETE /nosbieres/{id}

Supprime une bière.

---

## Notations

### GET /notations

Liste les notations.

### POST /notations

Ajoute une note.

---

## Photos

### GET /photos

Liste les métadonnées des photos.

### POST /photos

Upload une nouvelle photo (multipart/form-data).

### GET /photos/{id}

Télécharge la photo binaire.

### DELETE /photos/{id}

Supprime la photo.

---

## Marchandises

### GET /marchandises

Liste les marchandises.

### POST /marchandises

Crée une marchandise.

---

## Événements


### Get /evenements 

Liste les evenements.

### POST /evenements

Crée une evenements.

---

## Notes

* Les erreurs retournent un objet `{ code, message }`.
* La pagination utilise `?page=` et `?per_page=`.

---

**Fin du document.**
