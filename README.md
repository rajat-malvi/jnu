# JNU Jaipur Login Portal

A custom Flask-based login portal with in-memory user authentication.

## Local Setup

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Test Credentials

- **student1** / pass123
- **admin** / admin123
- **student2** / rajat

## Docker Setup

Build the image:
```bash
docker build -t jnu-login .
```

Run the container:
```bash
docker run -p 5000:5000 jnu-login
```

## Free Deployment Platforms

### 1. **Render** (Recommended)
- Free tier: 750 hours/month
- Auto-deploy from GitHub
- https://render.com
- Deploy: Connect GitHub repo → New Web Service → Use Dockerfile

### 2. **Railway**
- $5 free credit monthly
- Simple setup
- https://railway.app
- Deploy: New Project → Deploy from GitHub

### 3. **Fly.io**
- Free tier: 3 shared VMs
- Global deployment
- https://fly.io
```bash
fly launch
fly deploy
```

### 4. **Koyeb**
- Free tier available
- Docker support
- https://koyeb.com

### 5. **Google Cloud Run**
- Free tier: 2 million requests/month
- Pay-as-you-go after
- https://cloud.google.com/run

## Quick Deploy to Render

1. Push code to GitHub
2. Visit render.com and sign in
3. New → Web Service
4. Connect your repo
5. Select "Docker" as environment
6. Deploy!
