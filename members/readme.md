{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <link rel="icon" type="image/png" href="/static/images/favicon.png">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>À propos - FondAction SARL</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #0f172a;
}

.page {
    min-height: 100vh;
    padding: 28px 26px 60px;
}

.topbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-bottom: 70px;
}

.back-btn {
    width: 54px;
    height: 54px;
    border: none;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.back-btn svg {
    width: 32px;
    height: 32px;
}

.content {
    max-width: 760px;
    margin: 0 auto;
}

.title {
    margin: 0;
    text-align: center;
    font-size: clamp(52px, 10vw, 86px);
    line-height: 1.05;
    font-weight: 900;
    color: #0f172a;
}

.title-line {
    width: 128px;
    height: 7px;
    border-radius: 999px;
    margin: 24px auto 64px;
    display: flex;
    overflow: hidden;
}

.title-line span {
    flex: 1;
}

.line-green {
    background: #178a37;
}

.line-yellow {
    background: #f59e0b;
}

.line-red {
    background: #dc2626;
}

.text {
    color: #0f172a;
    font-size: clamp(24px, 5vw, 36px);
    line-height: 1.55;
    font-weight: 500;
}

.text p {
    margin: 0 0 42px;
}

.text strong {
    font-weight: 900;
}

@media (max-width: 600px) {
    .page {
        padding: 24px 22px 54px;
    }

    .topbar {
        margin-bottom: 62px;
    }

    .back-btn {
        width: 50px;
        height: 50px;
    }

    .title-line {
        margin-bottom: 58px;
    }

    .text p {
        margin-bottom: 38px;
    }
}
</style>
</head>

<body>

<div class="page">

    <div class="topbar">
        <button class="back-btn" type="button" onclick="history.back()" aria-label="Retour">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
            </svg>
        </button>
    </div>

    <main class="content">
        <h1 class="title">À propos</h1>

        <div class="title-line">
            <span class="line-green"></span>
            <span class="line-yellow"></span>
            <span class="line-red"></span>
        </div>

        <div class="text">
            <p>
                FondAction SARL est une initiative collective qui transforme les contributions individuelles
                en opportunités concrètes et durables.
            </p>

            <p>
                Notre objectif est de rassembler des personnes autour d’un système structuré capable de créer
                de la valeur à partir de l’effort collectif.
            </p>

            <p>
                Grâce aux contributions des membres, FondAction finance des projets utiles, soutient des initiatives
                et développe des solutions accessibles à tous.
            </p>

            <p>
                Notre mission est de permettre à chaque membre de participer à un système fiable, sécurisé
                et transparent.
            </p>

            <p>
                Nous croyons en une communauté forte, capable de construire son propre avenir et de transformer
                ses ressources en richesse durable.
            </p>

            <p>
                Chez FondAction, chaque membre compte.<br>
                Chaque contribution a un impact réel.
            </p>
        </div>
    </main>

</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logs d'activité</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }

        .header {
            background: white;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }

        .header h1 {
            margin: 0 0 10px 0;
            font-size: 32px;
            color: #111827;
        }

        .header-links a {
            text-decoration: none;
            margin-right: 15px;
            font-weight: bold;
            color: #2563eb;
        }

        .table-box {
            background: white;
            border-radius: 18px;
            padding: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            text-align: left;
            padding: 14px;
            background: #f9fafb;
            font-size: 14px;
            color: #111827;
        }

        td {
            padding: 14px;
            border-top: 1px solid #eee;
            font-size: 14px;
            color: #374151;
            vertical-align: top;
        }

        tr:hover {
            background: #f9fafb;
        }

        .action-badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            background: #dbeafe;
            color: #1d4ed8;
        }

        .details-box {
            max-width: 420px;
            line-height: 1.5;
            color: #4b5563;
        }

        .date-box {
            white-space: nowrap;
            color: #6b7280;
            font-size: 13px;
        }

        .admin-email {
            font-weight: bold;
            color: #111827;
        }

        .empty-box {
            text-align: center;
            padding: 24px;
            color: #6b7280;
        }
    </style>
</head>
<body>

<div class="page">

    <div class="header">
        <h1>📊 Logs d'activité</h1>

        <div class="header-links">
            <a href="/admins/dashboard/">← Dashboard</a>
        </div>
    </div>

    <div class="table-box">
        <table>
            <tr>
                <th>ID</th>
                <th>Admin</th>
                <th>Action</th>
                <th>Détails</th>
                <th>Date</th>
            </tr>

            {% for log in logs %}
            <tr>
                <td>{{ log.id }}</td>
                <td><span class="admin-email">{{ log.admin_user.email }}</span></td>
                <td><span class="action-badge">{{ log.action }}</span></td>
                <td><div class="details-box">{{ log.details }}</div></td>
                <td><span class="date-box">{{ log.created_at }}</span></td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5" class="empty-box">Aucun log disponible</td>
            </tr>
            {% endfor %}
        </table>
    </div>

</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Changer mot de passe admin</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 420px;
            background: white;
            border-radius: 20px;
            padding: 35px 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.25);
        }

        h1 {
            margin-top: 0;
            font-size: 26px;
            color: #111827;
            text-align: center;
        }

        p {
            text-align: center;
            color: #6b7280;
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 14px;
            border-radius: 12px;
            border: 1px solid #d1d5db;
            font-size: 15px;
            margin-bottom: 16px;
        }

        .btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 12px;
            background: #16a34a;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🔐 Changer votre mot de passe</h1>
    <p>Vous devez définir un nouveau mot de passe avant d’accéder au dashboard.</p>

    <form method="POST">
        {% csrf_token %}

        <label>Nouveau mot de passe</label>
        <input type="password" name="new_password" required>

        <label>Confirmer le mot de passe</label>
        <input type="password" name="confirm_password" required>

        <button type="submit" class="btn">Valider</button>
    </form>
</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Détail administrateur</title>
    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.94);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #1d4ed8;
            --primary-dark: #1e40af;
            --success-bg: #dcfce7;
            --success-text: #166534;
            --danger-bg: #fee2e2;
            --danger-text: #991b1b;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --radius-xl: 24px;
            --radius-lg: 18px;
            --radius-md: 14px;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(14, 165, 233, 0.08), transparent 30%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
            color: var(--text);
        }

        .page {
            max-width: 1320px;
            margin: 28px auto;
            padding: 20px;
        }

        .topbar {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #1d4ed8 100%);
            color: white;
            border-radius: 30px;
            padding: 28px;
            box-shadow: var(--shadow);
            margin-bottom: 22px;
            position: relative;
            overflow: hidden;
        }

        .topbar::after {
            content: "";
            position: absolute;
            width: 280px;
            height: 280px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            top: -120px;
            right: -80px;
        }

        .topbar small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.8;
            margin-bottom: 10px;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 34px;
            line-height: 1.2;
        }

        .topbar p {
            margin: 0;
            max-width: 760px;
            color: rgba(255,255,255,0.86);
            line-height: 1.6;
        }

        .top-actions {
            margin-top: 18px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .card {
            background: var(--card);
            backdrop-filter: blur(10px);
            border-radius: var(--radius-xl);
            padding: 24px;
            box-shadow: var(--shadow);
            border: 1px solid rgba(255,255,255,0.7);
            margin-bottom: 22px;
        }

        .section-title {
            margin: 0 0 18px 0;
            font-size: 22px;
        }

        .muted {
            color: var(--muted);
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: 0.2s ease;
            font-size: 14px;
        }

        .btn:hover {
            transform: translateY(-1px);
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        .btn-light {
            background: #e2e8f0;
            color: #0f172a;
        }

        .btn-success {
            background: #16a34a;
            color: white;
        }

        .btn-outline {
            background: white;
            color: var(--primary);
            border: 1px solid #bfdbfe;
        }

        .admin-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 22px;
            margin-bottom: 22px;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(220px, 1fr));
            gap: 14px;
        }

        .info-box {
            background: #f8fafc;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 15px 16px;
        }

        .info-box span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 7px;
        }

        .info-box strong {
            font-size: 16px;
            color: var(--text);
        }

        .status {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: bold;
        }

        .status-active {
            background: var(--success-bg);
            color: var(--success-text);
        }

        .status-suspended {
            background: var(--danger-bg);
            color: var(--danger-text);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(180px, 1fr));
            gap: 18px;
            margin-bottom: 22px;
        }

        .stat-card {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 22px;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.05);
        }

        .stat-card span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        .stat-card strong {
            font-size: 34px;
            line-height: 1;
            display: block;
            margin-bottom: 8px;
        }

        .stat-card p {
            margin: 0;
            color: var(--muted);
            font-size: 14px;
        }

        .filters-wrap {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 18px;
            align-items: end;
        }

        .filters-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(180px, 1fr));
            gap: 14px;
        }

        .field label {
            display: block;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #334155;
        }

        .field input,
        .field select {
            width: 100%;
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid #cbd5e1;
            background: white;
            font-size: 14px;
            outline: none;
        }

        .field input:focus,
        .field select:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
        }

        .filter-actions,
        .export-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .toolbar {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }

        .table-card {
            overflow: hidden;
            padding: 0;
        }

        .table-head {
            padding: 22px 24px 14px;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 980px;
        }

        thead th {
            text-align: left;
            font-size: 13px;
            color: #475569;
            background: #f8fafc;
            padding: 16px 18px;
            border-bottom: 1px solid var(--line);
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        tbody td {
            padding: 18px;
            border-bottom: 1px solid #eef2f7;
            font-size: 14px;
            vertical-align: middle;
        }

        tbody tr:hover {
            background: #f8fbff;
        }

        .member-name {
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 4px;
        }

        .member-sub {
            color: var(--muted);
            font-size: 13px;
        }

        .badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .badge-paid {
            background: var(--success-bg);
            color: var(--success-text);
        }

        .badge-unpaid {
            background: var(--danger-bg);
            color: var(--danger-text);
        }

        .empty-state {
            padding: 32px 24px 36px;
            text-align: center;
            color: var(--muted);
        }

        @media (max-width: 1024px) {
            .admin-grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .filters-wrap {
                grid-template-columns: 1fr;
            }

            .filters-grid {
                grid-template-columns: 1fr;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 640px) {
            .page {
                padding: 14px;
            }

            .topbar {
                padding: 22px;
                border-radius: 24px;
            }

            .topbar h1 {
                font-size: 28px;
            }

            .card {
                padding: 18px;
                border-radius: 20px;
            }

            .toolbar {
                align-items: stretch;
            }

            .filter-actions,
            .export-actions,
            .top-actions {
                flex-direction: column;
            }

            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>

<div class="page">
    <div class="topbar">
        <small>Administration • Performance détaillée</small>
        <h1>👤 Détail administrateur</h1>
        <p>
            Analyse complète des membres créés par cet administrateur sur la période choisie,
            avec distinction claire entre membres ayant payé et membres n’ayant pas payé.
        </p>

        <div class="top-actions">
            <a href="/admins/list/" class="btn btn-outline">← Retour à la liste</a>
            <a href="/admins/admins/{{ admin_obj.id }}/reset-password/" class="btn btn-success">
                Réinitialiser le mot de passe
            </a>
        </div>
    </div>

    <div class="admin-grid">
        <div class="card">
            <h2 class="section-title">Informations de l’administrateur</h2>

            <div class="info-grid">
                <div class="info-box">
                    <span>NIM</span>
                    <strong>{{ admin_obj.nim }}</strong>
                </div>

                <div class="info-box">
                    <span>Rôle</span>
                    <strong>{{ admin_obj.role }}</strong>
                </div>

                <div class="info-box">
                    <span>Nom</span>
                    <strong>{{ admin_obj.last_name }}</strong>
                </div>

                <div class="info-box">
                    <span>Prénom</span>
                    <strong>{{ admin_obj.first_name }}</strong>
                </div>

                <div class="info-box">
                    <span>Téléphone</span>
                    <strong>{{ admin_obj.phone|default:"Non renseigné" }}</strong>
                </div>

                <div class="info-box">
                    <span>Email</span>
                    <strong>{{ admin_obj.email }}</strong>
                </div>

                <div class="info-box">
                    <span>Date de création</span>
                    <strong>{{ admin_obj.created_at|date:"d/m/Y à H:i" }}</strong>
                </div>

                <div class="info-box">
                    <span>Statut</span>
                    <strong>
                        {% if admin_obj.status == 'active' %}
                            <span class="status status-active">Actif</span>
                        {% else %}
                            <span class="status status-suspended">Suspendu</span>
                        {% endif %}
                    </strong>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="section-title">Résumé de la période</h2>
            <p class="muted" style="margin-top: 0; line-height: 1.6;">
                Ces chiffres portent uniquement sur les membres créés dans la période sélectionnée.
                Ensuite, on distingue parmi eux ceux qui ont payé et ceux qui n’ont pas payé.
            </p>

            <div class="info-grid">
                <div class="info-box">
                    <span>Date début</span>
                    <strong>{{ start_date|default:"Toute l’historique" }}</strong>
                </div>

                <div class="info-box">
                    <span>Date fin</span>
                    <strong>{{ end_date|default:"Toute l’historique" }}</strong>
                </div>

                <div class="info-box">
                    <span>Filtre paiement</span>
                    <strong>
                        {% if payment_status == 'paid' %}
                            Ont payé
                        {% elif payment_status == 'unpaid' %}
                            N’ont pas payé
                        {% else %}
                            Tous
                        {% endif %}
                    </strong>
                </div>

                <div class="info-box">
                    <span>Export rapide</span>
                    <strong>Excel disponible ci-dessous</strong>
                </div>
            </div>
        </div>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <span>Total membres créés</span>
            <strong>{{ total_created_members }}</strong>
            <p>Membres créés dans la période filtrée</p>
        </div>

        <div class="stat-card">
            <span>Membres ayant payé</span>
            <strong>{{ total_paid_members }}</strong>
            <p>Au moins un paiement validé</p>
        </div>

        <div class="stat-card">
            <span>Membres n’ayant pas payé</span>
            <strong>{{ total_unpaid_members }}</strong>
            <p>Aucun paiement validé enregistré</p>
        </div>
    </div>

    <div class="card">
        <div class="toolbar">
            <div>
                <h2 class="section-title" style="margin-bottom: 6px;">Filtres d’analyse</h2>
                <div class="muted">Filtrer par date de création des membres puis par statut de paiement.</div>
            </div>
        </div>

        <form method="get">
            <div class="filters-wrap">
                <div class="filters-grid">
                    <div class="field">
                        <label for="start_date">Date début</label>
                        <input type="date" id="start_date" name="start_date" value="{{ start_date }}">
                    </div>

                    <div class="field">
                        <label for="end_date">Date fin</label>
                        <input type="date" id="end_date" name="end_date" value="{{ end_date }}">
                    </div>

                    <div class="field">
                        <label for="payment_status">Statut de paiement</label>
                        <select id="payment_status" name="payment_status">
                            <option value="all" {% if payment_status == 'all' %}selected{% endif %}>Tous</option>
                            <option value="paid" {% if payment_status == 'paid' %}selected{% endif %}>Ont payé</option>
                            <option value="unpaid" {% if payment_status == 'unpaid' %}selected{% endif %}>N’ont pas payé</option>
                        </select>
                    </div>
                </div>

                <div class="filter-actions">
                    <button type="submit" class="btn btn-primary">Appliquer les filtres</button>
                    <a href="/admins/admins/{{ admin_obj.id }}/" class="btn btn-light">Réinitialiser</a>
                </div>
            </div>
        </form>
    </div>

    <div class="card">
        <div class="toolbar">
            <div>
                <h2 class="section-title" style="margin-bottom: 6px;">Exports Excel</h2>
                <div class="muted">Télécharger la liste complète, les payés ou les non payés sur la période choisie.</div>
            </div>

            <div class="export-actions">
                <a href="/admins/admins/{{ admin_obj.id }}/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=all"
                   class="btn btn-dark">
                    Exporter tout
                </a>

                <a href="/admins/admins/{{ admin_obj.id }}/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=paid"
                   class="btn btn-success">
                    Exporter les payés
                </a>

                <a href="/admins/admins/{{ admin_obj.id }}/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=unpaid"
                   class="btn btn-outline">
                    Exporter les non payés
                </a>
            </div>
        </div>
    </div>

    <div class="card table-card">
        <div class="table-head">
            <h2 class="section-title" style="margin-bottom: 6px;">Membres créés par cet administrateur</h2>
            <div class="muted">
                Tableau construit sur la date de création des membres, avec indication de paiement.
            </div>
        </div>

        {% if members %}
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>NIM</th>
                            <th>Membre</th>
                            <th>Téléphone</th>
                            <th>Ville</th>
                            <th>Date de création</th>
                            <th>Statut paiement</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for member in members %}
                            <tr>
                                <td><strong>{{ member.nim }}</strong></td>
                                <td>
                                    <div class="member-name">{{ member.last_name }} {{ member.first_name }}</div>
                                    <div class="member-sub">Pièce : {{ member.id_card_type }}{% if member.id_card_number %} • {{ member.id_card_number }}{% endif %}</div>
                                </td>
                                <td>{{ member.phone|default:"Non renseigné" }}</td>
                                <td>{{ member.city|default:"Non renseignée" }}</td>
                                <td>{{ member.created_at|date:"d/m/Y à H:i" }}</td>
                                <td>
                                    {% if member.has_paid %}
                                        <span class="badge badge-paid">A payé</span>
                                    {% else %}
                                    <span class="badge badge-unpaid">N’a pas payé</span>
                                    {% endif %}
                                </td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="empty-state">
                Aucun membre trouvé pour les filtres sélectionnés.
            </div>
        {% endif %}
    </div>
</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Contrôle paiement admin</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            margin: 0;
            color: #111827;
        }

        .page {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }

        .card {
            background: white;
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }

        h1, h2 {
            margin-top: 0;
        }

        p {
            color: #374151;
            line-height: 1.6;
        }

        .btn {
            display: inline-block;
            padding: 10px 14px;
            border-radius: 8px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            margin-right: 10px;
            border: none;
            cursor: pointer;
        }

        .btn-green {
            background: #16a34a;
        }

        .btn-blue {
            background: #2563eb;
        }

        .btn-gray {
            background: #374151;
        }

        .badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .badge-admin {
            background: #dbeafe;
            color: #1d4ed8;
        }

        .badge-super {
            background: #ede9fe;
            color: #6d28d9;
        }

        .search-form {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: end;
            margin-top: 18px;
        }

        .field {
            flex: 1;
            min-width: 280px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #d1d5db;
            font-size: 14px;
            box-sizing: border-box;
        }

        .summary-box {
            margin-top: 18px;
            padding: 16px;
            border-radius: 12px;
            background: #f9fafb;
            color: #374151;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 14px;
            border-bottom: 1px solid #eee;
            text-align: left;
        }

        th {
            background: #f9fafb;
        }

        .empty-box {
            text-align: center;
            padding: 20px;
            color: #6b7280;
            font-weight: bold;
        }
    </style>
</head>
<body>
<div class="page">

    <div class="card">
        <a class="btn btn-gray" href="/admins/admins/payment-control/">← Retour</a>

        <h1>👤 Contrôle de {{ admin_obj.first_name }} {{ admin_obj.last_name }}</h1>

        <p><strong>NIM :</strong> {{ admin_obj.nim }}</p>
        <p><strong>Email :</strong> {{ admin_obj.email }}</p>
        <p>
            <strong>Rôle :</strong>
            {% if admin_obj.role == 'super_admin' %}
                <span class="badge badge-super">Super Admin</span>
            {% else %}
                <span class="badge badge-admin">Admin</span>
            {% endif %}
        </p>

        <div class="summary-box">
    <p><strong>Total payeurs ce mois :</strong> {{ paid_count }}</p>
    <p><strong>Total non payeurs ce mois :</strong> {{ unpaid_count }}</p>
    <p><strong>Montant total payé ce mois :</strong> {{ total_paid_amount }} FCFA</p>

    <a class="btn btn-green" href="/admins/admins/{{ admin_obj.id }}/payment-control/paid/export/">
        Exporter payeurs
    </a>
    <a class="btn btn-blue" href="/admins/admins/{{ admin_obj.id }}/payment-control/unpaid/export/">
        Exporter non payeurs
    </a>
</div>

        <form method="GET" class="search-form">
            <div class="field">
                <label>Recherche membre</label>
                <input
                    type="text"
                    name="member_search"
                    value="{{ member_search }}"
                    placeholder="NIM, nom, prénom ou téléphone"
                >
            </div>

            <button type="submit" class="btn btn-blue">Rechercher</button>

            <a class="btn btn-green" href="/admins/admins/{{ admin_obj.id }}/payment-control/">
                Réinitialiser
            </a>
        </form>
    </div>

    <div class="card">
        <h2>✅ Membres ayant payé ce mois</h2>
        <table>
            <tr>
                <th>NIM</th>
                <th>Nom</th>
                <th>Prénom</th>
                <th>Téléphone</th>
                <th>Ville</th>
            </tr>
            {% for member in paid_members %}
            <tr>
                <td>{{ member.nim }}</td>
                <td>{{ member.last_name }}</td>
                <td>{{ member.first_name }}</td>
                <td>{{ member.phone }}</td>
                <td>{{ member.city }}</td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5" class="empty-box">Aucun membre payeur ce mois</td>
            </tr>
            {% endfor %}
        </table>
    </div>

    <div class="card">
        <h2>❌ Membres n’ayant pas payé ce mois</h2>
        <table>
            <tr>
                <th>NIM</th>
                <th>Nom</th>
                <th>Prénom</th>
                <th>Téléphone</th>
                <th>Ville</th>
            </tr>
            {% for member in unpaid_members %}
            <tr>
                <td>{{ member.nim }}</td>
                <td>{{ member.last_name }}</td>
                <td>{{ member.first_name }}</td>
                <td>{{ member.phone }}</td>
                <td>{{ member.city }}</td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5" class="empty-box">Tous les membres ont payé ce mois</td>
            </tr>
            {% endfor %}
        </table>
    </div>

</div>
</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Détail des réalisations admin</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }

        .header, .filter-box, .table-box, .summary-box {
            background: white;
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }

        .header h1 {
            margin: 0 0 10px 0;
            font-size: 32px;
        }

        .header a {
            text-decoration: none;
            color: #2563eb;
            font-weight: bold;
        }

        form {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            align-items: end;
        }

        .field {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        label {
            font-weight: bold;
            color: #374151;
        }

        input {
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            font-size: 14px;
        }

        button, .btn-export {
            padding: 12px 18px;
            border: none;
            border-radius: 10px;
            background: #2563eb;
            color: white;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 14px;
            border-bottom: 1px solid #eee;
            text-align: left;
        }

        th {
            background: #f9fafb;
        }
    </style>
</head>
<body>

<div class="page">
    <div class="header">
        <h1>📊 Réalisation de {{ admin_obj.first_name }} {{ admin_obj.last_name }}</h1>
        <a href="/admins/admins/performance/">← Retour aux réalisations</a>
    </div>

    <div class="summary-box">
        <p><strong>NIM :</strong> {{ admin_obj.nim }}</p>
        <p><strong>Email :</strong> {{ admin_obj.email }}</p>
        <p><strong>Rôle :</strong> {{ admin_obj.role }}</p>
        <p><strong>Total de membres enregistrés sur la période :</strong> {{ total_members }}</p>
    </div>

    <div class="filter-box">
        <form method="GET">
            <div class="field">
                <label>Date début</label>
                <input type="date" name="start_date" value="{{ start_date }}">
            </div>

            <div class="field">
                <label>Date fin</label>
                <input type="date" name="end_date" value="{{ end_date }}">
            </div>

            <button type="submit">Filtrer</button>

            <a class="btn-export" href="/admins/admins/{{ admin_obj.id }}/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}">
                Export Excel
            </a>
        </form>
    </div>

    <div class="table-box">
        <table>
            <tr>
                <th>NIM membre</th>
                <th>Nom</th>
                <th>Prénom</th>
                <th>Téléphone</th>
                <th>Date création</th>
            </tr>

            {% for member in members %}
            <tr>
                <td>{{ member.nim }}</td>
                <td>{{ member.last_name }}</td>
                <td>{{ member.first_name }}</td>
                <td>{{ member.phone }}</td>
                <td>{{ member.created_at|date:"d/m/Y à H:i" }}</td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5">Aucun membre trouvé sur cette période</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Réalisations des administrateurs</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }

        .header, .filter-box, .table-box {
            background: white;
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }

        .table-box {
            overflow-x: auto;
        }

        .header h1 {
            margin: 0 0 10px 0;
            font-size: 32px;
        }

        .header a {
            text-decoration: none;
            color: #2563eb;
            font-weight: bold;
        }

        form {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            align-items: end;
        }

        .field {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        label {
            font-weight: bold;
            color: #374151;
        }

        input {
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            font-size: 14px;
        }

        button {
            padding: 12px 18px;
            border: none;
            border-radius: 10px;
            background: #2563eb;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 1150px;
        }

        th, td {
            padding: 14px;
            border-bottom: 1px solid #eee;
            text-align: left;
            vertical-align: top;
        }

        th {
            background: #f9fafb;
        }

        .btn-detail {
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 8px;
            background: #16a34a;
            color: white;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
            margin-right: 6px;
            margin-bottom: 6px;
        }

        .btn-blue {
            background: #2563eb;
        }

        .empty-box {
            text-align: center;
            padding: 24px;
            color: #6b7280;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="page">
    <div class="header">
        <h1>📈 Réalisations des admins et super admins</h1>
        <a href="/admins/dashboard/">← Retour dashboard</a>
    </div>

    <div class="filter-box">
        <form method="GET">
            <div class="field">
                <label>Date début</label>
                <input type="date" name="start_date" value="{{ start_date }}">
            </div>

            <div class="field">
                <label>Date fin</label>
                <input type="date" name="end_date" value="{{ end_date }}">
            </div>

            <div class="field">
                <label>Recherche admin</label>
                <input type="text" name="search" value="{{ search }}" placeholder="Nom, prénom, email, NIM">
            </div>

            <button type="submit">Filtrer</button>

            <a href="/admins/admins/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&search={{ search }}"
               style="padding: 12px 18px; border-radius: 10px; background: #16a34a; color: white; font-weight: bold; text-decoration: none; display: inline-block;">
                Export Excel
            </a>
        </form>
    </div>

    <div class="header" style="margin-top: 20px;">
        <h2 style="margin:0; font-size: 24px;">📊 Total général des réalisations</h2>

        {% if start_date or end_date %}
            <p style="margin-top:10px; font-size:18px; color:#374151;">
                Sur la période sélectionnée,
                tous les admins et super admins ont enregistré
                <strong style="color:#16a34a;">{{ grand_total_members }}</strong> membre(s).
            </p>
        {% else %}
            <p style="margin-top:10px; font-size:18px; color:#374151;">
                Depuis le début,
                tous les admins et super admins ont enregistré
                <strong style="color:#16a34a;">{{ grand_total_members }}</strong> membre(s).
            </p>
        {% endif %}

        <p style="margin-top:10px; font-size:18px; color:#374151;">
            <strong>Payeurs sur la période :</strong> {{ grand_total_paid_members }}<br>
            <strong>Non payeurs sur la période :</strong> {{ grand_total_unpaid_members }}<br>
            <strong>Montant total payé sur la période :</strong> {{ grand_total_paid_amount }} FCFA
        </p>
    </div>

    <div class="table-box">
        <table>
            <tr>
                <th>NIM</th>
                <th>Nom</th>
                <th>Prénom</th>
                <th>Email</th>
                <th>Rôle</th>
                <th>Statut</th>
                <th>Membres créés</th>
                <th>Payeurs</th>
                <th>Non payeurs</th>
                <th>Montant payé</th>
                <th>Action</th>
            </tr>

            {% for item in performance_data %}
            <tr>
                <td>{{ item.admin.nim }}</td>
                <td>{{ item.admin.last_name }}</td>
                <td>{{ item.admin.first_name }}</td>
                <td>{{ item.admin.email }}</td>
                <td>{{ item.admin.role }}</td>
                <td>{{ item.admin.status }}</td>
                <td>{{ item.total_members }}</td>
                <td>{{ item.paid_count }}</td>
                <td>{{ item.unpaid_count }}</td>
                <td>{{ item.total_paid_amount }} FCFA</td>
                <td>
                    <a href="/admins/admins/{{ item.admin.id }}/" class="btn-detail btn-blue">
                        Voir profil
                    </a>

                    <a href="/admins/admins/{{ item.admin.id }}/payment-control/" class="btn-detail">
                        Voir contrôle
                    </a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="11" class="empty-box">Aucune donnée trouvée</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Espace administrateur</title>
    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.95);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --success: #16a34a;
            --danger: #dc2626;
            --warning: #d97706;
            --purple: #7c3aed;
            --cyan: #0891b2;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --radius-xl: 28px;
            --radius-lg: 22px;
            --radius-md: 16px;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
        }

        .page {
            max-width: 1320px;
            margin: 32px auto;
            padding: 20px;
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #2563eb 100%);
            color: white;
            border-radius: 32px;
            padding: 34px 32px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
        }

        .hero::before {
            content: "";
            position: absolute;
            top: -80px;
            right: -70px;
            width: 240px;
            height: 240px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .hero::after {
            content: "";
            position: absolute;
            bottom: -90px;
            left: -70px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: rgba(255,255,255,0.05);
        }

        .hero small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.82;
            margin-bottom: 12px;
        }

        .hero h1 {
            margin: 0 0 10px;
            font-size: 36px;
            line-height: 1.15;
            position: relative;
            z-index: 1;
        }

        .hero p {
            margin: 0;
            max-width: 820px;
            line-height: 1.7;
            color: rgba(255,255,255,0.88);
            position: relative;
            z-index: 1;
        }

        .hero-actions {
            margin-top: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            position: relative;
            z-index: 1;
        }

        .hero-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 14px;
            transition: 0.2s ease;
        }

        .hero-btn:hover {
            transform: translateY(-1px);
        }

        .hero-btn-light {
            background: white;
            color: #0f172a;
        }

        .hero-btn-outline {
            background: rgba(255,255,255,0.12);
            color: white;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .section-card {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: var(--radius-xl);
            padding: 24px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
            backdrop-filter: blur(10px);
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }

        .section-head h2 {
            margin: 0 0 6px;
            font-size: 24px;
        }

        .section-head p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-box {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 20px;
            min-height: 120px;
        }

        .stat-box span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        .stat-box strong {
            display: block;
            font-size: 30px;
            line-height: 1.1;
            margin-bottom: 8px;
        }

        .stat-box p {
            margin: 0;
            color: var(--muted);
            font-size: 14px;
            line-height: 1.5;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(240px, 1fr));
            gap: 20px;
        }

        .card {
            display: block;
            text-decoration: none;
            color: var(--text);
            background: white;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
            border: 1px solid var(--line);
            transition: 0.22s ease;
            min-height: 210px;
            position: relative;
            overflow: hidden;
        }

        .card::after {
            content: "";
            position: absolute;
            right: -20px;
            top: -20px;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            opacity: 0.08;
            background: currentColor;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.10);
        }

        .card .icon {
            width: 58px;
            height: 58px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
            background: rgba(15, 23, 42, 0.06);
        }

        .card h3 {
            margin: 0 0 10px;
            font-size: 22px;
            line-height: 1.3;
        }

        .card p {
            margin: 0;
            color: var(--muted);
            line-height: 1.7;
            font-size: 14.5px;
        }

        .card-tag {
            display: inline-block;
            margin-top: 16px;
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            background: #eff6ff;
            color: #1d4ed8;
        }

        .card-blue { color: var(--primary); }
        .card-green { color: var(--success); }
        .card-purple { color: var(--purple); }
        .card-cyan { color: var(--cyan); }
        .card-orange { color: var(--warning); }
        .card-red { color: var(--danger); }

        .bottom-actions {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            padding: 13px 18px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 14px;
            transition: 0.2s ease;
        }

        .btn:hover {
            transform: translateY(-1px);
        }

        .btn-back {
            background: #e5e7eb;
            color: #111827;
        }

        .btn-logout {
            background: var(--danger);
            color: white;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        @media (max-width: 1100px) {
            .grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 760px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 24px 22px;
                border-radius: 24px;
            }

            .hero h1 {
                font-size: 28px;
            }

            .section-card {
                padding: 18px;
                border-radius: 22px;
            }

            .card {
                min-height: auto;
            }

            .hero-actions,
            .bottom-actions {
                flex-direction: column;
            }

            .hero-btn,
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="page">
        <div class="hero">
            <small>Administration • Espace de pilotage</small>
            <h1>Espace administrateur</h1>
            <p>
                Retrouvez ici toutes les actions liées à la gestion des administrateurs, au suivi des réalisations,
                aux journaux d’activité, aux retraits, aux publications et au contrôle global des performances.
            </p>

            <div class="hero-actions">
                <a href="/admins/dashboard/" class="hero-btn hero-btn-light">Retour au dashboard</a>
                <a href="/admins/admins/performance/" class="hero-btn hero-btn-outline">Voir la performance globale</a>
            </div>
        </div>

        <div class="section-card">
            <div class="section-head">
                <div>
                    <h2>Pilotage rapide</h2>
                    <p>Accédez rapidement aux principaux modules de gestion de l’espace administrateur.</p>
                </div>
            </div>

            <div class="stats-grid">
                <div class="stat-box">
                    <span>Gestion</span>
                    <strong>Admins</strong>
                    <p>Créer, consulter et suivre les comptes administrateurs.</p>
                </div>

                <div class="stat-box">
                    <span>Suivi</span>
                    <strong>Performance</strong>
                    <p>Observer les réalisations individuelles et globales.</p>
                </div>

                <div class="stat-box">
                    <span>Contrôle</span>
                    <strong>Logs</strong>
                    <p>Consulter les traces d’activité importantes du système.</p>
                </div>

                <div class="stat-box">
                    <span>Opérations</span>
                    <strong>Retraits</strong>
                    <p>Traiter les demandes de retrait et les recherches transactionnelles.</p>
                </div>
            </div>

            <div class="grid">
                <a href="/admins/list/" class="card card-blue">
                    <div class="icon">👨‍💼</div>
                    <h3>Liste des admins</h3>
                    <p>Consulter tous les administrateurs enregistrés sur la plateforme, accéder à leurs détails et suivre leurs réalisations.</p>
                    <span class="card-tag">Gestion des comptes</span>
                </a>

                <a href="/admins/create/" class="card card-green">
                    <div class="icon">➕</div>
                    <h3>Créer un admin</h3>
                    <p>Ajouter un nouvel administrateur au système avec son compte, son rôle et les informations utiles à son suivi.</p>
                    <span class="card-tag">Création rapide</span>
                </a>

                <a href="/admins/admins/performance/" class="card card-purple">
                    <div class="icon">📈</div>
                    <h3>Performance globale</h3>
                    <p>Voir tous les membres créés sur une période, ceux qui ont payé, ceux qui n’ont pas payé et l’admin créateur correspondant.</p>
                    <span class="card-tag">Vue générale</span>
                </a>

                <a href="/admins/logs/" class="card card-cyan">
                    <div class="icon">📊</div>
                    <h3>Logs d’activité</h3>
                    <p>Consulter l’historique détaillé des actions effectuées dans le système pour un meilleur contrôle administratif.</p>
                    <span class="card-tag">Traçabilité</span>
                </a>

                <a href="/admins/info-posts/create/" class="card card-orange">
                    <div class="icon">📝</div>
                    <h3>Faire un post</h3>
                    <p>Publier une nouvelle information, annonce ou communication destinée aux membres depuis l’espace administratif.</p>
                    <span class="card-tag">Publication</span>
                </a>

                <a href="/admins/info-posts/" class="card card-blue">
                    <div class="icon">🗂️</div>
                    <h3>Gérer les posts</h3>
                    <p>Modifier, organiser et suivre les publications déjà créées afin de garder une communication bien structurée.</p>
                    <span class="card-tag">Contenu</span>
                </a>

                <a href="/admins/withdrawal-requests/" class="card card-red">
                    <div class="icon">💸</div>
                    <h3>Demandes de retrait</h3>
                    <p>Consulter les demandes en attente, les approuver ou les rejeter, et suivre le traitement des opérations de retrait.</p>
                    <span class="card-tag">Validation</span>
                </a>

                <a href="/admins/search-transactions/" class="card card-cyan">
                    <div class="icon">🔎</div>
                    <h3>Rechercher les transactions</h3>
                    <p>Retrouver rapidement une transaction précise grâce à la recherche par reçu ou informations disponibles.</p>
                    <span class="card-tag">Recherche</span>
                </a>
            </div>
        </div>

        <div class="section-card">
            <div class="section-head">
                <div>
                    <h2>Actions rapides</h2>
                    <p>Accès direct aux actions générales de navigation et de session.</p>
                </div>
            </div>

            <div class="bottom-actions">
                <a href="/admins/dashboard/" class="btn btn-back">Retour au dashboard</a>
                <a href="/admins/admins/performance/" class="btn btn-primary">Ouvrir la page globale</a>
                <a href="/admins/logout/" class="btn btn-logout">Se déconnecter</a>
            </div>
        </div>
    </div>
</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des admins</title>

    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.96);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --success: #16a34a;
            --danger: #dc2626;
            --purple: #7c3aed;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
            color: var(--text);
        }

        .page {
            max-width: 1380px;
            margin: 30px auto;
            padding: 20px;
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #2563eb 100%);
            color: white;
            border-radius: 30px;
            padding: 30px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
        }

        .hero::after {
            content: "";
            position: absolute;
            top: -90px;
            right: -80px;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .hero small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.82;
            margin-bottom: 10px;
        }

        .hero h1 {
            margin: 0 0 10px 0;
            font-size: 36px;
            line-height: 1.15;
            position: relative;
            z-index: 1;
        }

        .hero p {
            margin: 0;
            max-width: 840px;
            line-height: 1.7;
            color: rgba(255,255,255,0.88);
            position: relative;
            z-index: 1;
        }

        .hero-actions {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 20px;
            position: relative;
            z-index: 1;
        }

        .hero-btn,
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 14px;
            border: none;
            cursor: pointer;
            transition: 0.2s ease;
        }

        .hero-btn:hover,
        .btn:hover {
            transform: translateY(-1px);
        }

        .hero-btn-light {
            background: white;
            color: #0f172a;
        }

        .hero-btn-outline {
            background: rgba(255,255,255,0.12);
            color: white;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .section-card {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: 26px;
            padding: 24px;
            box-shadow: var(--shadow);
            margin-bottom: 22px;
            backdrop-filter: blur(10px);
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }

        .section-head h2 {
            margin: 0 0 6px;
            font-size: 24px;
        }

        .section-head p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .search-form {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 16px;
            align-items: end;
        }

        .search-fields {
            display: grid;
            grid-template-columns: minmax(260px, 380px);
            gap: 14px;
        }

        .field label {
            display: block;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #334155;
        }

        .field input {
            width: 100%;
            padding: 13px 14px;
            border-radius: 14px;
            border: 1px solid #cbd5e1;
            background: white;
            font-size: 14px;
            outline: none;
        }

        .field input:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
        }

        .search-actions,
        .bottom-actions,
        .table-actions {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
        }

        .btn-light {
            background: #e2e8f0;
            color: #0f172a;
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        .btn-success {
            background: var(--success);
            color: white;
        }

        .btn-danger {
            background: var(--danger);
            color: white;
        }

        .btn-purple {
            background: var(--purple);
            color: white;
        }

        .table-box {
            background: white;
            border-radius: 22px;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
            border: 1px solid var(--line);
            overflow: hidden;
        }

        .table-top {
            padding: 22px 22px 14px;
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
        }

        .table-top h3 {
            margin: 0 0 6px;
            font-size: 22px;
        }

        .table-top p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 1180px;
        }

        th {
            text-align: left;
            padding: 16px 18px;
            background: #f8fafc;
            font-size: 13px;
            color: #334155;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            border-bottom: 1px solid var(--line);
        }

        td {
            padding: 18px;
            border-top: 1px solid #eef2f7;
            font-size: 14px;
            color: #334155;
            vertical-align: middle;
        }

        tr:hover {
            background: #f8fbff;
        }

        .admin-name {
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 4px;
        }

        .admin-sub {
            color: var(--muted);
            font-size: 13px;
        }

        .role-badge,
        .status-badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .role-super {
            background: #ede9fe;
            color: #6d28d9;
        }

        .role-admin {
            background: #dbeafe;
            color: #1d4ed8;
        }

        .status-active {
            background: #dcfce7;
            color: #166534;
        }

        .status-suspended {
            background: #fee2e2;
            color: #991b1b;
        }

        .action-group {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .btn-sm {
            padding: 9px 12px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: bold;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .btn-view {
            background: #eff6ff;
            color: #1d4ed8;
        }

        .btn-reset {
            background: #dcfce7;
            color: #166534;
        }

        .btn-suspend {
            background: #fee2e2;
            color: #991b1b;
        }

        .btn-reactivate {
            background: #dcfce7;
            color: #166534;
        }

        .protected {
            color: #94a3b8;
            font-style: italic;
            font-size: 12px;
            font-weight: bold;
        }

        .empty-box {
            text-align: center;
            padding: 28px;
            color: var(--muted);
        }

        .footer-actions {
            margin-top: 20px;
        }

        @media (max-width: 980px) {
            .search-form {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 760px) {
            .page {
                padding: 14px;
            }

            .hero {
                padding: 24px 22px;
                border-radius: 24px;
            }

            .hero h1 {
                font-size: 28px;
            }

            .section-card {
                padding: 18px;
                border-radius: 22px;
            }

            .hero-actions,
            .search-actions,
            .bottom-actions,
            .table-actions {
                flex-direction: column;
            }

            .hero-btn,
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>

<div class="page">

    <div class="hero">
        <small>Administration • Gestion des comptes</small>
        <h1>📋 Liste des admins</h1>
        <p>
            Consultez les administrateurs enregistrés, recherchez rapidement un compte par NIM,
            accédez aux détails, réinitialisez les mots de passe et gérez les statuts de façon claire et élégante.
        </p>

        <div class="hero-actions">
            <a href="/admins/dashboard/" class="hero-btn hero-btn-light">← Retour au dashboard</a>
            <a href="/admins/create/" class="hero-btn hero-btn-outline">➕ Créer un admin</a>
            <a href="/admins/admins/performance/" class="hero-btn hero-btn-outline">📈 Réalisations des admins</a>
        </div>
    </div>

    <div class="section-card">
        <div class="section-head">
            <div>
                <h2>Recherche rapide</h2>
                <p>Retrouver un administrateur à partir de son NIM.</p>
            </div>
        </div>

        <form method="get" class="search-form">
            <div class="search-fields">
                <div class="field">
                    <label for="nim">NIM de l’administrateur</label>
                    <input
                        type="text"
                        id="nim"
                        name="nim"
                        value="{{ search_nim }}"
                        placeholder="Exemple : FAS-0000000012">
                </div>
            </div>

            <div class="search-actions">
                <button type="submit" class="btn btn-primary">Rechercher</button>
                <a href="/admins/list/" class="btn btn-light">Réinitialiser</a>
            </div>
        </form>
    </div>
    <div class="table-box">
        <div class="table-top">
            <div>
                <h3>Administrateurs enregistrés</h3>
                <p>Liste complète des comptes admins avec accès rapide aux actions principales.</p>
            </div>

            <div class="table-actions">
                <a href="/admins/admins/export/" class="btn btn-dark">📥 Exporter la liste des admins</a>
                <a href="/admins/admins/performance/" class="btn btn-purple">📈 Ouvrir les réalisations</a>
            </div>
        </div>

        <div class="table-wrap">
            <table>
                <tr>
                    <th>ID</th>
                    <th>NIM</th>
                    <th>Administrateur</th>
                    <th>Email</th>
                    <th>Rôle</th>
                    <th>Statut</th>
                    <th>Action</th>
                </tr>

                {% for admin in admins %}
                <tr>
                    <td>{{ admin.id }}</td>
                    <td><strong>{{ admin.nim }}</strong></td>

                    <td>
                        <div class="admin-name">{{ admin.last_name }} {{ admin.first_name }}</div>
                        <div class="admin-sub">
                            {% if admin.phone %}
                                {{ admin.phone }}
                            {% else %}
                                Téléphone non renseigné
                            {% endif %}
                        </div>
                    </td>

                    <td>{{ admin.email }}</td>

                    <td>
                        {% if admin.role == 'super_admin' %}
                            <span class="role-badge role-super">Super Admin</span>
                        {% else %}
                            <span class="role-badge role-admin">Admin</span>
                        {% endif %}
                    </td>

                    <td>
                        {% if admin.status == 'active' %}
                            <span class="status-badge status-active">Actif</span>
                        {% else %}
                            <span class="status-badge status-suspended">Suspendu</span>
                        {% endif %}
                    </td>

                    <td>
                        <div class="action-group">
                            <a href="/admins/admins/{{ admin.id }}/" class="btn-sm btn-view">
                                Voir plus
                            </a>

                            {% if admin.email != 'admin@fondaction.com' %}
                                <a href="/admins/admins/{{ admin.id }}/reset-password/" class="btn-sm btn-reset">
                                    Réinitialiser mot de passe
                                </a>
                            {% endif %}

                            {% if admin.email != 'admin@fondaction.com' and admin.role != 'super_admin' %}
                                {% if admin.status == 'active' %}
                                    <a href="/admins/suspend/{{ admin.id }}/" class="btn-sm btn-suspend">
                                        Suspendre
                                    </a>
                                {% elif admin.status == 'suspended' %}
                                    <a href="/admins/reactivate/{{ admin.id }}/" class="btn-sm btn-reactivate">
                                        Réactiver
                                    </a>
                                {% endif %}
                            {% else %}
                                <span class="protected">Protégé</span>
                            {% endif %}
                        </div>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="7" class="empty-box">
                        Aucun administrateur trouvé.
                    </td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>

    <div class="section-card footer-actions">
        <div class="section-head">
            <div>
                <h2>Accès rapides</h2>
                <p>Navigation rapide vers les actions principales liées aux administrateurs.</p>
            </div>
        </div>

        <div class="bottom-actions">
            <a href="/admins/dashboard/" class="btn btn-light">Retour au dashboard</a>
            <a href="/admins/create/" class="btn btn-primary">Créer un admin</a>
            <a href="/admins/admins/export/" class="btn btn-dark">Exporter la liste</a>
            <a href="/admins/admins/performance/" class="btn btn-purple">Voir les réalisations</a>
        </div>
    </div>

</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <link rel="icon" type="image/png" href="/static/images/favicon.png">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact - FondAction SARL</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #0f172a;
}

.page {
    min-height: 100vh;
    padding: 28px 26px 60px;
}

.topbar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 58px;
}

.back-btn {
    width: 54px;
    height: 54px;
    border: none;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.back-btn svg {
    width: 32px;
    height: 32px;
}

.content {
    max-width: 820px;
    margin: 0 auto;
}

.title {
    margin: 0;
    text-align: center;
    font-size: clamp(52px, 10vw, 86px);
    line-height: 1.05;
    font-weight: 900;
    color: #0f172a;
}

.title-line {
    width: 128px;
    height: 7px;
    border-radius: 999px;
    margin: 24px auto 48px;
    display: flex;
    overflow: hidden;
}

.title-line span { flex: 1; }
.line-green { background: #178a37; }
.line-yellow { background: #f59e0b; }
.line-red { background: #dc2626; }

.intro {
    margin: 0 auto 44px;
    color: #263244;
    font-size: clamp(22px, 4.8vw, 34px);
    line-height: 1.5;
    font-weight: 500;
    text-align: center;
}

.cards {
    display: grid;
    gap: 22px;
}

.contact-card {
    text-decoration: none;
    color: #0f172a;
    background: #ffffff;
    border: 1px solid #e8eef0;
    border-radius: 24px;
    padding: 24px;
    display: grid;
    grid-template-columns: 72px 1fr;
    gap: 22px;
    align-items: center;
    box-shadow: 0 14px 28px rgba(15, 23, 42, 0.07);
}

.icon-box {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: #eef9f0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-box svg {
    width: 38px;
    height: 38px;
}

.icon-box svg path,
.icon-box svg .cls-1 {
    stroke: #178a37;
    fill: none;
}

.icon-box.call svg path,
.icon-box.email svg path {
    fill: #178a37;
    stroke: none;
}

.card-title {
    margin: 0 0 8px;
    color: #178a37;
    font-size: clamp(22px, 4.8vw, 32px);
    line-height: 1.2;
    font-weight: 900;
}

.card-text {
    margin: 0;
    color: #263244;
    font-size: clamp(18px, 4vw, 26px);
    line-height: 1.4;
    font-weight: 600;
    word-break: break-word;
}

.note {
    margin: 38px 0 0;
    padding: 24px;
    border-radius: 22px;
    background: rgba(23, 138, 55, 0.06);
    border: 1px solid rgba(23, 138, 55, 0.18);
    color: #263244;
    font-size: clamp(19px, 4.2vw, 28px);
    line-height: 1.5;
    font-weight: 500;
}

.note strong {
    color: #178a37;
    font-weight: 900;
}

@media (max-width: 600px) {
    .page {
        padding: 24px 22px 54px;
    }

    .topbar {
        margin-bottom: 52px;
    }

    .back-btn {
        width: 50px;
        height: 50px;
    }

    .contact-card {
        grid-template-columns: 62px 1fr;
        gap: 18px;
        padding: 20px;
    }

    .icon-box {
        width: 62px;
        height: 62px;
    }

    .icon-box svg {
        width: 34px;
        height: 34px;
    }
}
</style>
</head>

<body>

<div class="page">

    <div class="topbar">
        <button class="back-btn" type="button" onclick="history.back()" aria-label="Retour">
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
            </svg>
        </button>
    </div>

    <main class="content">
        <h1 class="title">Contact</h1>

        <div class="title-line">
            <span class="line-green"></span>
            <span class="line-yellow"></span>
            <span class="line-red"></span>
        </div>

        <p class="intro">
            L’administration FondAction est disponible pour vous accompagner,
            répondre à vos questions et vous orienter dans vos démarches.
        </p>

        <div class="cards">
            <a href="tel:+2290160212109" class="contact-card">
                <div class="icon-box call">
                    <svg viewBox="0 0 24 24" fill="none">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M17.3545 22.2323C15.3344 21.7262 11.1989 20.2993 7.44976 16.5502C3.70065 12.8011 2.2738 8.66559 1.76767 6.6455C1.47681 5.48459 2.00058 4.36434 2.88869 3.72997L5.21694 2.06693C6.57922 1.09388 8.47432 1.42407 9.42724 2.80051L10.893 4.91776C11.5152 5.8165 11.3006 7.0483 10.4111 7.68365L9.24234 8.51849C9.41923 9.1951 9.96939 10.5846 11.6924 12.3076C13.4154 14.0306 14.8049 14.5807 15.4815 14.7576L16.3163 13.5888C16.9517 12.6994 18.1835 12.4847 19.0822 13.1069L21.1995 14.5727C22.5759 15.5257 22.9061 17.4207 21.933 18.783L20.27 21.1113C19.6356 21.9994 18.5154 22.5232 17.3545 22.2323ZM8.86397 15.136C12.2734 18.5454 16.0358 19.8401 17.8405 20.2923C18.1043 20.3583 18.4232 20.2558 18.6425 19.9488L20.3056 17.6205C20.6299 17.1665 20.5199 16.5348 20.061 16.2171L17.9438 14.7513L17.0479 16.0056C16.6818 16.5182 16.0047 16.9202 15.2163 16.7501C14.2323 16.5378 12.4133 15.8569 10.2782 13.7218C8.1431 11.5867 7.46219 9.7677 7.24987 8.7837C7.07977 7.9953 7.48181 7.31821 7.99439 6.95208L9.24864 6.05618L7.78285 3.93893C7.46521 3.48011 6.83351 3.37005 6.37942 3.6944L4.05117 5.35744C3.74413 5.57675 3.64162 5.89565 3.70771 6.15943C4.15989 7.96418 5.45459 11.7266 8.86397 15.136Z"></path>
                    </svg>
                </div>

                <div>
                    <h2 class="card-title">Appel</h2>
                    <p class="card-text">+229 01 60 21 21 09</p>
                </div>
            </a>

            <a href="https://wa.me/2290160212109" class="contact-card">
                <div class="icon-box">
                    <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                        <path class="cls-1" d="M24,2.5A21.52,21.52,0,0,0,5.15,34.36L2.5,45.5l11.14-2.65A21.5,21.5,0,1,0,24,2.5ZM13.25,12.27h5.86a1,1,0,0,1,1,1,10.4,10.4,0,0,0,.66,3.91,1.93,1.93,0,0,1-.66,2.44l-2.05,2a18.6,18.6,0,0,0,3.52,4.79A18.6,18.6,0,0,0,26.35,30l2-2.05c1-1,1.46-1,2.44-.66a10.4,10.4,0,0,0,3.91.66,1.05,1.05,0,0,1,1,1v5.86a1.05,1.05,0,0,1-1,1,23.68,23.68,0,0,1-15.64-6.84,23.6,23.6,0,0,1-6.84-15.64A1.07,1.07,0,0,1,13.25,12.27Z"></path>
                    </svg>
                </div>

                <div>
                    <h2 class="card-title">WhatsApp</h2>
                    <p class="card-text">Écrire à l’administration</p>
                </div>
            </a>

            <a href="mailto:contact@fondactionsarl.com" class="contact-card">
                <div class="icon-box email">
                    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                        <path d="M510.678,112.275c-2.308-11.626-7.463-22.265-14.662-31.054c-1.518-1.915-3.104-3.63-4.823-5.345 c-12.755-12.818-30.657-20.814-50.214-20.814H71.021c-19.557,0-37.395,7.996-50.21,20.814c-1.715,1.715-3.301,3.43-4.823,5.345 C8.785,90.009,3.63,100.649,1.386,112.275C0.464,116.762,0,121.399,0,126.087V385.92c0,9.968,2.114,19.55,5.884,28.203 c3.497,8.26,8.653,15.734,14.926,22.001c1.59,1.586,3.169,3.044,4.892,4.494c12.286,10.175,28.145,16.32,45.319,16.32h369.958 c17.18,0,33.108-6.145,45.323-16.384c1.718-1.386,3.305-2.844,4.891-4.43c6.27-6.267,11.425-13.741,14.994-22.001v-0.064 c3.769-8.653,5.812-18.171,5.812-28.138V126.087C512,121.399,511.543,116.762,510.678,112.275z M46.509,101.571 c6.345-6.338,14.866-10.175,24.512-10.175h369.958c9.646,0,18.242,3.837,24.512,10.175c1.122,1.129,2.179,2.387,3.112,3.637 L274.696,274.203c-5.348,4.687-11.954,7.002-18.696,7.002c-6.674,0-13.276-2.315-18.695-7.002L43.472,105.136 C44.33,103.886,45.387,102.7,46.509,101.571z M36.334,385.92V142.735L176.658,265.15L36.405,387.435 C36.334,386.971,36.334,386.449,36.334,385.92z M440.979,420.597H71.021c-6.281,0-12.158-1.651-17.174-4.552l147.978-128.959 l13.815,12.018c11.561,10.046,26.028,15.134,40.36,15.134c14.406,0,28.872-5.088,40.432-15.134l13.808-12.018l147.92,128.959 C453.137,418.946,447.26,420.597,440.979,420.597z M475.666,385.92c0,0.529,0,1.051-0.068,1.515L335.346,265.221L475.666,142.8 V385.92z"></path>
                    </svg>
                </div>

                <div>
                    <h2 class="card-title">Email</h2>
                    <p class="card-text">contact@fondactionsarl.com</p>
                </div>
            </a>
        </div>

        <div class="note">
            <strong>Information :</strong> toutes les demandes liées aux comptes, à l’inscription,
            aux paiements ou à l’assistance doivent être adressées à l’administration FondAction.
        </div>
    </main>

</div>

</body>
</html>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un admin</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
        }

        .header {
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            color: white;
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2);
        }

        .header h1 {
            margin: 0;
            font-size: 32px;
        }

        .form-card {
            background: white;
            border-radius: 18px;
            padding: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        }

        .form-card h3 {
            margin-top: 0;
            margin-bottom: 20px;
            font-size: 22px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            color: #111827;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .full {
            grid-column: span 2;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #374151;
        }

        input,
        select {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #d1d5db;
            font-size: 14px;
            outline: none;
        }

        input:focus,
        select:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }

        .note {
            margin-top: 18px;
            padding: 14px;
            background: #f9fafb;
            border-radius: 12px;
            color: #4b5563;
            line-height: 1.5;
            font-size: 14px;
        }

        .actions {
            display: flex;
            gap: 15px;
            margin-top: 22px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 14px 22px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            font-size: 15px;
            text-decoration: none;
        }

        .btn-primary {
            background: #2563eb;
            color: white;
        }

        .btn-secondary {
            background: #e5e7eb;
            color: #111827;
        }

        @media (max-width: 800px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .full {
                grid-column: span 1;
            }
        }
    </style>
</head>
<body>

<div class="page">

    <div class="header">
        <h1>➕ Créer un administrateur</h1>
    </div>

    <form method="POST">
    {% csrf_token %}

    <div class="form-card">
        <h3>Informations de l’administrateur</h3>

        <div class="grid">
            <div class="full">
                <label>NIM du membre</label>
                <div style="display:flex; gap:10px;">
                    <input type="text" id="nim" name="nim" required placeholder="Ex: FAS-0000000001">
                    <button type="button" class="btn btn-secondary" onclick="fetchMemberByNim()">Vérifier NIM</button>
                </div>
            </div>

            <div>
                <label>Prénom</label>
                <input type="text" id="preview_first_name" readonly>
            </div>

            <div>
                <label>Nom</label>
                <input type="text" id="preview_last_name" readonly>
            </div>

            <div class="full">
                <label>Téléphone</label>
                <input type="text" id="preview_phone" readonly>
            </div>

            <div class="full">
                <label>Email administrateur</label>
                <input type="email" name="email" required>
            </div>

            <div class="full">
                <label>Rôle</label>
                <select name="role" required>
                    <option value="admin">Admin</option>
                    <option value="super_admin">Super Admin</option>
                </select>
            </div>
        </div>

        <div class="note">
            Le mot de passe est attribué automatiquement par le système. L’administrateur devra le changer à sa première connexion.
        </div>

        <div class="actions">
            <button type="submit" class="btn btn-primary">Créer</button>
            <a href="/admins/dashboard/" class="btn btn-secondary">Retour dashboard</a>
        </div>
    </div>
</form>

<script>
async function fetchMemberByNim() {
    const nim = document.getElementById('nim').value.trim();

    if (!nim) {
        alert("Veuillez saisir un NIM");
        return;
    }

    try {
        const response = await fetch(`/admins/api/member-by-nim/?nim=${encodeURIComponent(nim)}`);
        const data = await response.json();

        if (!data.success) {
            document.getElementById('preview_first_name').value = '';
            document.getElementById('preview_last_name').value = '';
            document.getElementById('preview_phone').value = '';
            alert(data.message || "Membre introuvable");
            return;
        }

        document.getElementById('preview_first_name').value = data.member.first_name || '';
        document.getElementById('preview_last_name').value = data.member.last_name || '';
        document.getElementById('preview_phone').value = data.member.phone || '';
    } catch (error) {
        alert("Erreur lors de la récupération du membre");
    }
}
</script>

</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer une publication</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
        }

        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        h1 {
            margin-top: 0;
            font-size: 28px;
            color: #111827;
        }

        .subtitle {
            color: #6b7280;
            margin-bottom: 25px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #111827;
        }

        input, textarea {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #d1d5db;
            font-size: 15px;
        }

        textarea {
            resize: vertical;
            min-height: 120px;
        }

        input[type="file"] {
            padding: 8px;
        }

        .btn {
            display: inline-block;
            padding: 14px 18px;
            border-radius: 12px;
            font-weight: bold;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
        }

        .btn-primary {
            background: #2563eb;
            color: white;
            border: none;
        }

        .btn-primary:hover {
            background: #1d4ed8;
        }

        .btn-secondary {
            background: #374151;
            color: white;
            margin-right: 10px;
        }

        .actions {
            margin-top: 20px;
        }

        .hint {
            font-size: 13px;
            color: #6b7280;
            margin-top: 5px;
        }

        .preview {
            margin-top: 20px;
            padding: 15px;
            border-radius: 12px;
            background: #f9fafb;
            border: 1px solid #e5e7eb;
        }

        .preview img {
            width: 100%;
            max-height: 250px;
            object-fit: cover;
            border-radius: 10px;
            margin-top: 10px;
        }

        @media (max-width: 768px) {
            .container {
                margin: 20px;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="card">

        <h1>Créer une publication</h1>
        <p class="subtitle">
            Publiez une information visible par tous les membres.
        </p>

        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}

            <!-- Titre -->
            <div class="form-group">
                <label>Titre</label>
                <input type="text" name="title" required placeholder="Ex : Nouvelle opportunité pour les membres">
            </div>

            <!-- Contenu -->
            <div class="form-group">
                <label>Contenu</label>
                <textarea name="content" required placeholder="Écris ici ton message..."></textarea>
            </div>

            <!-- Image -->
            <div class="form-group">
                <label>Image (optionnelle)</label>
                <input type="file" name="image" accept="image/*" onchange="previewImage(event)">
                <div class="hint">Formats autorisés : JPG, PNG</div>
            </div>

            <!-- Vidéo -->
            <div class="form-group">
                <label>Lien vidéo YouTube (optionnel)</label>
                <input type="url" name="video_url" placeholder="https://youtu.be/...">
                <div class="hint">
                    Colle simplement le lien YouTube (pas besoin de embed)
                </div>
            </div>

            <!-- Aperçu -->
            <div class="preview" id="imagePreview" style="display:none;">
                <strong>Aperçu image :</strong>
                <img id="previewImg">
            </div>

            <!-- Actions -->
            <div class="actions">
                <a href="/admins/admins-hub/" class="btn btn-secondary">← Retour</a>
                <button type="submit" class="btn btn-primary">Publier</button>
            </div>

        </form>

    </div>
</div>

<script>
function previewImage(event) {
    const preview = document.getElementById('imagePreview');
    const img = document.getElementById('previewImg');

    img.src = URL.createObjectURL(event.target.files[0]);
    preview.style.display = 'block';
}
</script>

</body>
</html>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un membre</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: #111827;
        }

        .page {
            max-width: 1120px;
            margin: 32px auto;
            padding: 20px;
        }

        .header {
            background: linear-gradient(135deg, #1d4ed8, #2563eb, #3b82f6);
            color: white;
            padding: 28px;
            border-radius: 22px;
            margin-bottom: 22px;
            box-shadow: 0 14px 28px rgba(37, 99, 235, 0.22);
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 18px;
            flex-wrap: wrap;
        }

        .header h1 {
            margin: 0 0 10px;
            font-size: 32px;
        }

        .header p {
            margin: 0;
            color: rgba(255, 255, 255, 0.92);
            line-height: 1.6;
            max-width: 760px;
        }

        .header-links {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .header-links a {
            text-decoration: none;
            padding: 12px 16px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        }

        .btn-back {
            background: rgba(255, 255, 255, 0.18);
            color: white;
        }

        .form-card {
            background: white;
            border-radius: 22px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        .form-card h3 {
            margin-top: 0;
            margin-bottom: 18px;
            font-size: 22px;
            border-bottom: 1px solid #edf2f7;
            padding-bottom: 10px;
            color: #0f172a;
        }

        .section-note {
            margin-top: -6px;
            margin-bottom: 18px;
            color: #6b7280;
            line-height: 1.6;
            font-size: 14px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .full {
            grid-column: span 2;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #374151;
            font-size: 14px;
        }

        input, select {
            width: 100%;
            padding: 13px 14px;
            border-radius: 12px;
            border: 1px solid #d1d5db;
            font-size: 14px;
            outline: none;
            background: white;
        }

        input:focus, select:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.10);
        }

        .help-text {
            margin-top: 6px;
            font-size: 12px;
            color: #6b7280;
            line-height: 1.5;
        }

        .actions {
            display: flex;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 14px 22px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            font-size: 14px;
            text-decoration: none;
        }

        .btn-primary {
            background: #2563eb;
            color: white;
        }

        .btn-secondary {
            background: #e5e7eb;
            color: #111827;
        }

        @media (max-width: 820px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .full {
                grid-column: span 1;
            }

            .header-top {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

<div class="page">

    <div class="header">
        <div class="header-top">
            <div>
                <h1>Enregistrer un membre</h1>
                <p>
                    Renseignez soigneusement les informations du membre.
                    Cette fiche servira à la création complète de son profil et de son accès à l’espace membre.
                </p>
            </div>

            <div class="header-links">
                <a href="/admins/members-hub/" class="btn-back">← Retour espace membres</a>
            </div>
        </div>
    </div>

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}

        <div class="form-card">
            <h3>Informations générales</h3>
            <div class="section-note">
                Informations d’identification personnelle du membre.
            </div>

            <div class="grid">
                <div>
                    <label for="first_name">Prénom</label>
                    <input id="first_name" type="text" name="first_name" required>
                </div>

                <div>
                    <label for="last_name">Nom</label>
                    <input id="last_name" type="text" name="last_name" required>
                </div>

                <div>
                    <label for="birth_date">Date de naissance</label>
                    <input id="birth_date" type="date" name="birth_date" required>
                </div>

                <div>
                    <label for="birth_place">Lieu de naissance</label>
                    <input id="birth_place" type="text" name="birth_place" required>
                </div>

                <div>
                    <label for="department">Département</label>
                    <input id="department" type="text" name="department" required>
                </div>

                <div>
                    <label for="commune">Commune</label>
                    <input id="commune" type="text" name="commune" required>
                </div>

                <div>
                    <label for="city">Ville</label>
                    <input id="city" type="text" name="city" required>
                </div>

                <div>
                    <label for="district">Quartier</label>
                    <input id="district" type="text" name="district" required>
                </div>

                <div class="full">
                    <label for="phone">Téléphone</label>
                    <input id="phone" type="text" name="phone" placeholder="Exemple : 0195404040">
                    <div class="help-text">
                        Le numéro doit être unique si tu l’utilises pour identifier le membre.
                    </div>
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Pièce d’identité</h3>
            <div class="section-note">
                Informations de la pièce utilisée pour enregistrer le membre.
            </div>

            <div class="grid">
                <div class="full">
                    <label for="id_card_type">Type de pièce</label>
                    <select id="id_card_type" name="id_card_type" required>
                        <option value="CIP">CIP</option>
                        <option value="NPI">NPI</option>
                        <option value="CEDEAO">CEDEAO</option>
                        <option value="PASSEPORT">PASSEPORT</option>
                    </select>
                </div>

                <div class="full">
                    <label for="id_card_number">Numéro de pièce / NPI</label>
                    <input id="id_card_number" type="text" name="id_card_number" required>
                </div>

                <div>
                    <label for="id_card_front">Photo recto</label>
                    <input id="id_card_front" type="file" name="id_card_front" accept="image/*" required>
                </div>

                <div>
                    <label for="id_card_back">Photo verso</label>
                    <input id="id_card_back" type="file" name="id_card_back" accept="image/*" required>
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Photo du membre</h3>
            <div class="section-note">
                Ajoute une photo d’identité claire du membre.
            </div>

            <label for="photo">Photo d’identité</label>
            <input id="photo" type="file" name="photo" accept="image/*" required>
        </div>

        <div class="form-card">
            <h3>Personne à contacter</h3>
            <div class="section-note">
                Informations de la personne à joindre en cas de besoin.
            </div>

            <div class="grid">
                <div>
                    <label for="emergency_last_name">Nom</label>
                    <input id="emergency_last_name" type="text" name="emergency_last_name" required>
                </div>

                <div>
                    <label for="emergency_first_name">Prénom</label>
                    <input id="emergency_first_name" type="text" name="emergency_first_name" required>
                </div>

                <div class="full">
                    <label for="emergency_phone">Téléphone</label>
                    <input id="emergency_phone" type="text" name="emergency_phone" required>
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Sécurité</h3>
            <div class="section-note">
                Définis le code PIN initial du membre.
            </div>

            <label for="member_pin">PIN membre (5 chiffres)</label>
            <input
                id="member_pin"
                type="password"
                name="member_pin"
                maxlength="5"
                inputmode="numeric"
                pattern="[0-9]{5}"
                required
            >
            <div class="help-text">
                Le PIN doit contenir exactement 5 chiffres.
            </div>
        </div>

        <div class="form-card">
            <h3>Signature finale</h3>
            <div class="section-note">
                La signature doit être fournie en format PNG.
            </div>

            <label for="signature">Signature (PNG uniquement)</label>
            <input id="signature" type="file" name="signature" accept="image/png" required>
        </div>

        <div class="actions">
            <button type="submit" class="btn btn-primary">Créer le membre</button>
            <a href="/admins/members-hub/" class="btn btn-secondary">Annuler</a>
        </div>

    </form>

</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Admin</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: #111827;
        }

        .page {
            max-width: 1100px;
            margin: 40px auto;
            padding: 20px;
        }

        .header-card {
            background: linear-gradient(135deg, #0f172a, #1d4ed8, #3b82f6);
            color: white;
            border-radius: 26px;
            padding: 32px;
            box-shadow: 0 16px 34px rgba(29, 78, 216, 0.24);
            margin-bottom: 34px;
            position: relative;
            overflow: hidden;
        }

        .header-card::after {
            content: "";
            position: absolute;
            right: -70px;
            top: -70px;
            width: 220px;
            height: 220px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 50%;
        }

        .header-card h1 {
            margin: 0 0 10px;
            font-size: 36px;
            position: relative;
            z-index: 1;
        }

        .header-card p {
            margin: 6px 0;
            font-size: 17px;
            position: relative;
            z-index: 1;
        }

        .badge {
            display: inline-block;
            margin-top: 14px;
            padding: 10px 16px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.15);
            font-weight: bold;
            font-size: 14px;
            position: relative;
            z-index: 1;
        }

        .welcome-box {
            margin-bottom: 24px;
        }

        .welcome-box h2 {
            margin: 0 0 8px;
            font-size: 28px;
            color: #0f172a;
        }

        .welcome-box p {
            margin: 0;
            color: #6b7280;
            line-height: 1.6;
            font-size: 15px;
        }

        .main-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }

        .main-card {
            display: block;
            text-decoration: none;
            background: white;
            border-radius: 28px;
            padding: 34px 28px;
            box-shadow: 0 14px 30px rgba(15, 23, 42, 0.08);
            border: 1px solid #e5e7eb;
            color: #111827;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            min-height: 260px;
        }

        .main-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.12);
        }

        .main-card .icon {
            width: 72px;
            height: 72px;
            border-radius: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 34px;
            margin-bottom: 22px;
        }

        .main-card.members .icon {
            background: #dcfce7;
        }

        .main-card.admins .icon {
            background: #dbeafe;
        }

        .main-card h3 {
            margin: 0 0 12px;
            font-size: 28px;
        }

        .main-card p {
            margin: 0 0 20px;
            color: #6b7280;
            line-height: 1.7;
            font-size: 15px;
        }

        .main-card .go {
            display: inline-block;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        }

        .main-card.members .go {
            background: #16a34a;
            color: white;
        }

        .main-card.admins .go {
            background: #2563eb;
            color: white;
        }

        .logout-box {
            margin-top: 34px;
            text-align: center;
        }

        .logout-btn {
            display: inline-block;
            text-decoration: none;
            background: #dc2626;
            color: white;
            padding: 14px 24px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0 10px 20px rgba(220, 38, 38, 0.18);
        }

        @media (max-width: 850px) {
            .main-grid {
                grid-template-columns: 1fr;
            }

            .header-card h1 {
                font-size: 30px;
            }
        }
    </style>
</head>
<body>

    <div class="page">
        <div class="header-card">
            <h1>Dashboard Administration</h1>
            <p><strong>Email :</strong> {{ email }}</p>
            <p><strong>Rôle :</strong> {{ role }}</p>
            <div class="badge">Interface sécurisée de gestion</div>
        </div>

        <div class="welcome-box">
            <h2>Choisissez un espace</h2>
            <p>
                Accédez rapidement à la gestion des membres ou à l’administration des comptes.
                Cette page a été simplifiée pour offrir une navigation claire, professionnelle et facile à prendre en main.
            </p>
        </div>

        <div class="main-grid">
            <a href="/admins/members-hub/" class="main-card members">
                <div class="icon">👥</div>
                <h3>Administration des membres</h3>
                <p>
                    Ouvrir l’espace dédié aux membres : enregistrement, consultation, historique,
                    connexion membre, transactions et autres opérations liées aux abonnés.
                </p>
                <span class="go">Ouvrir l’espace membres</span>
            </a>

            <a href="/admins/admins-hub/" class="main-card admins">
                <div class="icon">🛡️</div>
                <h3>Espace administrateur</h3>
                <p>
                    Ouvrir l’espace réservé à la gestion des administrateurs :
                    création, consultation, performances, suivi et journaux d’activité.
                </p>
                <span class="go">Ouvrir l’espace admins</span>
            </a>
        </div>

        <div class="logout-box">
            <a href="/admins/logout/" class="logout-btn">Se déconnecter</a>
        </div>
    </div>

</body>
</html>




<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modifier une publication</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
        }

        .container {
            max-width: 850px;
            margin: 40px auto;
            padding: 20px;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        h1 {
            margin-top: 0;
            font-size: 28px;
            color: #111827;
        }

        .subtitle {
            color: #6b7280;
            margin-bottom: 25px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #111827;
        }

        input, textarea {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #d1d5db;
            font-size: 15px;
        }

        textarea {
            resize: vertical;
            min-height: 130px;
        }

        input[type="file"] {
            padding: 8px;
        }

        .btn {
            display: inline-block;
            padding: 14px 18px;
            border-radius: 12px;
            font-weight: bold;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
            border: none;
        }

        .btn-primary {
            background: #2563eb;
            color: white;
        }

        .btn-secondary {
            background: #374151;
            color: white;
            margin-right: 10px;
        }

        .actions {
            margin-top: 20px;
        }

        .hint {
            font-size: 13px;
            color: #6b7280;
            margin-top: 5px;
        }

        .current-image {
            margin-top: 12px;
        }

        .current-image img {
            width: 100%;
            max-width: 280px;
            max-height: 220px;
            object-fit: cover;
            border-radius: 10px;
            border: 1px solid #ddd;
        }

        @media (max-width: 768px) {
            .container {
                margin: 20px;
            }

            .actions {
                display: flex;
                flex-direction: column;
                gap: 12px;
            }

            .btn-secondary,
            .btn-primary {
                width: 100%;
                margin-right: 0;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="card">
        <h1>Modifier une publication</h1>
        <p class="subtitle">Mets à jour le contenu de ton post puis enregistre les changements.</p>

        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}

            <div class="form-group">
                <label>Titre</label>
                <input type="text" name="title" value="{{ post.title }}" required>
            </div>

            <div class="form-group">
                <label>Contenu</label>
                <textarea name="content" required>{{ post.content }}</textarea>
            </div>

            <div class="form-group">
                <label>Lien vidéo YouTube (optionnel)</label>
                <input type="url" name="video_url" value="{{ post.video_url|default:'' }}">
                <div class="hint">Tu peux coller un lien YouTube normal.</div>
            </div>

            <div class="form-group">
                <label>Nouvelle image (optionnelle)</label>
                <input type="file" name="image" accept="image/*">
                <div class="hint">Si tu choisis une nouvelle image, elle remplacera l’ancienne.</div>

                {% if post.image %}
                    <div class="current-image">
                        <p><strong>Image actuelle :</strong></p>
                        <img src="{{ post.image.url }}" alt="{{ post.title }}">
                    </div>
                {% endif %}
            </div>

            <div class="actions">
                <a href="/admins/info-posts/" class="btn btn-secondary">← Retour</a>
                <button type="submit" class="btn btn-primary">Enregistrer les modifications</button>
            </div>
        </form>
    </div>
</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modifier un membre</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: #111827;
        }

        .page {
            max-width: 1120px;
            margin: 32px auto;
            padding: 20px;
        }

        .header {
            background: linear-gradient(135deg, #1d4ed8, #2563eb, #3b82f6);
            color: white;
            padding: 28px;
            border-radius: 22px;
            margin-bottom: 22px;
            box-shadow: 0 14px 28px rgba(37, 99, 235, 0.22);
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 18px;
            flex-wrap: wrap;
        }

        .header h1 {
            margin: 0 0 10px;
            font-size: 32px;
        }

        .header p {
            margin: 0;
            color: rgba(255, 255, 255, 0.92);
            line-height: 1.6;
            max-width: 760px;
        }

        .header-links {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .header-links a {
            text-decoration: none;
            padding: 12px 16px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        }

        .btn-back {
            background: rgba(255, 255, 255, 0.18);
            color: white;
        }

        .form-card {
            background: white;
            border-radius: 22px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        .form-card h3 {
            margin-top: 0;
            margin-bottom: 18px;
            font-size: 22px;
            border-bottom: 1px solid #edf2f7;
            padding-bottom: 10px;
            color: #0f172a;
        }

        .section-note {
            margin-top: -6px;
            margin-bottom: 18px;
            color: #6b7280;
            line-height: 1.6;
            font-size: 14px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .full {
            grid-column: span 2;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #374151;
            font-size: 14px;
        }

        input, select {
            width: 100%;
            padding: 13px 14px;
            border-radius: 12px;
            border: 1px solid #d1d5db;
            font-size: 14px;
            outline: none;
            background: white;
        }

        input:focus, select:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.10);
        }

        .help-text {
            margin-top: 6px;
            font-size: 12px;
            color: #6b7280;
            line-height: 1.5;
        }

        .actions {
            display: flex;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 14px 22px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
        }

        .btn-primary {
            background: #2563eb;
            color: white;
        }

        .btn-secondary {
            background: #e5e7eb;
            color: #111827;
        }

        @media (max-width: 820px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .full {
                grid-column: span 1;
            }

            .header-top {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

<div class="page">

    <div class="header">
        <div class="header-top">
            <div>
                <h1>Modifier un membre</h1>
                <p>
                    Mets à jour les informations du membre, ses documents
                    et ses coordonnées sans recréer une nouvelle fiche.
                </p>
            </div>

            <div class="header-links">
                <a href="/admins/members-hub/" class="btn-back">← Retour espace membres</a>
                <a href="/admins/members/{{ member.id }}/" class="btn-back">← Retour détail membre</a>
            </div>
        </div>
    </div>

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}

        <div class="form-card">
            <h3>Informations générales</h3>
            <div class="section-note">
                Modifie les informations personnelles principales du membre.
            </div>

            <div class="grid">
                <div>
                    <label for="first_name">Prénom</label>
                    <input id="first_name" type="text" name="first_name" value="{{ member.first_name }}" required>
                </div>

                <div>
                    <label for="last_name">Nom</label>
                    <input id="last_name" type="text" name="last_name" value="{{ member.last_name }}" required>
                </div>

                <div>
                    <label for="birth_date">Date de naissance</label>
                    <input id="birth_date" type="date" name="birth_date" value="{{ member.birth_date|date:'Y-m-d' }}" required>
                </div>

                <div>
                    <label for="birth_place">Lieu de naissance</label>
                    <input id="birth_place" type="text" name="birth_place" value="{{ member.birth_place }}" required>
                </div>

                <div>
                    <label for="department">Département</label>
                    <input id="department" type="text" name="department" value="{{ member.department }}" required>
                </div>

                <div>
                    <label for="commune">Commune</label>
                    <input id="commune" type="text" name="commune" value="{{ member.commune }}" required>
                </div>

                <div>
                    <label for="city">Ville</label>
                    <input id="city" type="text" name="city" value="{{ member.city }}" required>
                </div>

                <div>
                    <label for="district">Quartier</label>
                    <input id="district" type="text" name="district" value="{{ member.district }}" required>
                </div>

                <div class="full">
                    <label for="phone">Téléphone</label>
                    <input id="phone" type="text" name="phone" value="{{ member.phone }}">
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Pièce d’identité</h3>
            <div class="section-note">
                Mets à jour les informations de la pièce et remplace les documents si nécessaire.
            </div>

            <div class="grid">
                <div class="full">
                    <label for="id_card_type">Type de pièce</label>
                    <select id="id_card_type" name="id_card_type" required>
                        <option value="CIP" {% if member.id_card_type == 'CIP' %}selected{% endif %}>CIP</option>
                        <option value="NPI" {% if member.id_card_type == 'NPI' %}selected{% endif %}>NPI</option>
                        <option value="CEDEAO" {% if member.id_card_type == 'CEDEAO' %}selected{% endif %}>CEDEAO</option>
                        <option value="PASSEPORT" {% if member.id_card_type == 'PASSEPORT' %}selected{% endif %}>PASSEPORT</option>
                    </select>
                </div>

                <div class="full">
                    <label for="id_card_number">Numéro de pièce / NPI</label>
                    <input id="id_card_number" type="text" name="id_card_number" value="{{ member.id_card_number }}" required>
                </div>

                <div>
                    <label for="id_card_front">Nouveau recto (optionnel)</label>
                    <input id="id_card_front" type="file" name="id_card_front" accept="image/*">
                </div>

                <div>
                    <label for="id_card_back">Nouveau verso (optionnel)</label>
                    <input id="id_card_back" type="file" name="id_card_back" accept="image/*">
                </div>

                <div class="full">
                    <label for="photo">Nouvelle photo d’identité (optionnel)</label>
                    <input id="photo" type="file" name="photo" accept="image/*">
                </div>

                <div class="full">
                    <label for="signature">Nouvelle signature PNG (optionnel)</label>
                    <input id="signature" type="file" name="signature" accept="image/png">
                    <div class="help-text">
                        La signature doit être en format PNG si tu choisis de la remplacer.
                    </div>
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Personne à contacter</h3>
            <div class="section-note">
                Mets à jour les coordonnées de la personne à joindre en cas de besoin.
            </div>

            <div class="grid">
                <div>
                    <label for="emergency_last_name">Nom</label>
                    <input id="emergency_last_name" type="text" name="emergency_last_name" value="{{ member.emergency_last_name }}" required>
                </div>

                <div>
                    <label for="emergency_first_name">Prénom</label>
                    <input id="emergency_first_name" type="text" name="emergency_first_name" value="{{ member.emergency_first_name }}" required>
                </div>

                <div class="full">
                    <label for="emergency_phone">Téléphone</label>
                    <input id="emergency_phone" type="text" name="emergency_phone" value="{{ member.emergency_phone }}" required>
                </div>
            </div>
        </div>

        <div class="actions">
            <button type="submit" class="btn btn-primary">Enregistrer les modifications</button>
            <a href="/admins/members/{{ member.id }}/" class="btn btn-secondary">Annuler</a>
        </div>
    </form>

</div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Performance globale des administrateurs</title>
    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.94);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #1d4ed8;
            --primary-dark: #1e40af;
            --success-bg: #dcfce7;
            --success-text: #166534;
            --danger-bg: #fee2e2;
            --danger-text: #991b1b;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --radius-xl: 24px;
            --radius-lg: 18px;
            --radius-md: 14px;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(14, 165, 233, 0.08), transparent 30%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
        }

        .page {
            max-width: 1460px;
            margin: 28px auto;
            padding: 20px;
        }

        .topbar {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #1d4ed8 100%);
            color: white;
            border-radius: 30px;
            padding: 30px;
            box-shadow: var(--shadow);
            margin-bottom: 22px;
            position: relative;
            overflow: hidden;
        }

        .topbar::after {
            content: "";
            position: absolute;
            width: 320px;
            height: 320px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            top: -130px;
            right: -90px;
        }

        .topbar small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.8;
            margin-bottom: 10px;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 36px;
            line-height: 1.2;
        }

        .topbar p {
            margin: 0;
            max-width: 900px;
            color: rgba(255,255,255,0.88);
            line-height: 1.6;
        }

        .top-actions {
            margin-top: 18px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .card {
            background: var(--card);
            backdrop-filter: blur(10px);
            border-radius: var(--radius-xl);
            padding: 24px;
            box-shadow: var(--shadow);
            border: 1px solid rgba(255,255,255,0.7);
            margin-bottom: 22px;
        }

        .section-title {
            margin: 0 0 18px 0;
            font-size: 22px;
        }

        .muted {
            color: var(--muted);
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: 0.2s ease;
            font-size: 14px;
        }

        .btn:hover {
            transform: translateY(-1px);
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        .btn-light {
            background: #e2e8f0;
            color: #0f172a;
        }

        .btn-outline {
            background: white;
            color: var(--primary);
            border: 1px solid #bfdbfe;
        }

        .summary-grid {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 22px;
            margin-bottom: 22px;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(220px, 1fr));
            gap: 14px;
        }

        .info-box {
            background: #f8fafc;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 15px 16px;
        }

        .info-box span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 7px;
        }

        .info-box strong {
            font-size: 16px;
            color: var(--text);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(6, minmax(180px, 1fr));
            gap: 18px;
            margin-bottom: 22px;
        }

        .stat-card {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 22px;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.05);
        }

        .stat-card span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        .stat-card strong {
            font-size: 30px;
            line-height: 1.1;
            display: block;
            margin-bottom: 8px;
        }

        .stat-card p {
            margin: 0;
            color: var(--muted);
            font-size: 14px;
        }

        .filters-wrap {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 18px;
            align-items: end;
        }

        .filters-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(180px, 1fr));
            gap: 14px;
        }

        .field label {
            display: block;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #334155;
        }

        .field input,
        .field select {
            width: 100%;
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid #cbd5e1;
            background: white;
            font-size: 14px;
            outline: none;
        }

        .filter-actions,
        .export-actions,
        .top-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .toolbar {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }

        .table-card {
            overflow: hidden;
            padding: 0;
        }

        .table-head {
            padding: 22px 24px 14px;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 1280px;
        }

        thead th {
            text-align: left;
            font-size: 13px;
            color: #475569;
            background: #f8fafc;
            padding: 16px 18px;
            border-bottom: 1px solid var(--line);
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        tbody td {
            padding: 18px;
            border-bottom: 1px solid #eef2f7;
            font-size: 14px;
            vertical-align: middle;
        }

        tbody tr:hover {
            background: #f8fbff;
        }

        .member-name,
        .admin-name {
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 4px;
        }

        .member-sub,
        .admin-sub {
            color: var(--muted);
            font-size: 13px;
        }

        .badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .badge-paid {
            background: var(--success-bg);
            color: var(--success-text);
        }

        .badge-unpaid {
            background: var(--danger-bg);
            color: var(--danger-text);
        }

        .money {
            font-weight: bold;
            color: #0f172a;
        }

        .empty-state {
            padding: 34px 24px 40px;
            text-align: center;
            color: var(--muted);
        }

        .hidden-row {
            display: none;
        }

        .see-more-wrap {
            padding: 18px 24px 24px;
            display: flex;
            justify-content: center;
        }

        .toggle-btn {
            background: #eff6ff;
            color: var(--primary);
            border: 1px solid #bfdbfe;
        }

        @media (max-width: 1200px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .summary-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 1024px) {
            .filters-wrap {
                grid-template-columns: 1fr;
            }

            .filters-grid {
                grid-template-columns: 1fr;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 640px) {
            .page {
                padding: 14px;
            }

            .topbar {
                padding: 22px;
                border-radius: 24px;
            }

            .topbar h1 {
                font-size: 28px;
            }

            .card {
                padding: 18px;
                border-radius: 20px;
            }

            .filter-actions,
            .export-actions,
            .top-actions {
                flex-direction: column;
            }

            .btn {
                width: 100%;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<div class="page">
    <div class="topbar">
        <small>Administration • Suivi global</small>
        <h1>📊 Performance globale des administrateurs</h1>
        <p>
            Cette vue affiche tous les membres créés sur la période choisie, leur statut de paiement,
            le montant total déjà payé et l’administrateur qui les a créés.
        </p>

        <div class="top-actions">
            <a href="/admins/dashboard/" class="btn btn-outline">← Retour au dashboard</a>
            <a href="/admins/admins/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status={{ payment_status }}"
               class="btn btn-dark">
                Exporter la vue actuelle
            </a>
        </div>
    </div>

    <div class="summary-grid">
        <div class="card">
            <h2 class="section-title">Résumé de l’analyse globale</h2>
            <p class="muted" style="margin-top: 0; line-height: 1.6;">
                On filtre les membres selon leur date de création, puis on observe parmi eux ceux qui ont payé ou non,
                avec l’admin créateur affiché directement dans le tableau.
            </p>

            <div class="info-grid">
                <div class="info-box">
                    <span>Date début</span>
                    <strong>{{ start_date|default:"Toute l’historique" }}</strong>
                </div>

                <div class="info-box">
                    <span>Date fin</span>
                    <strong>{{ end_date|default:"Toute l’historique" }}</strong>
                </div>

                <div class="info-box">
                    <span>Filtre paiement</span>
                    <strong>
                        {% if payment_status == 'paid' %}
                            Ont payé
                        {% elif payment_status == 'unpaid' %}
                            N’ont pas payé
                        {% else %}
                            Tous
                        {% endif %}
                    </strong>
                </div>

                <div class="info-box">
                    <span>Vue affichée</span>
                    <strong>Membres + admin + paiements</strong>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="section-title">Lecture métier</h2>
            <p class="muted" style="margin-top: 0; line-height: 1.7;">
                Aucun membre créé dans la période n’est masqué. Même s’il n’a pas payé, il reste visible.
                Cette page permet aussi de suivre globalement la production des admins.
            </p>

            <div class="info-grid">
                <div class="info-box">
                    <span>Export</span>
                    <strong>Excel global disponible</strong>
                </div>

                <div class="info-box">
                    <span>Logique</span>
                    <strong>Date création → statut paiement</strong>
                </div>
            </div>
        </div>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <span>Total admins</span>
            <strong>{{ total_admins }}</strong>
            <p>Nombre total d’administrateurs</p>
        </div>

        <div class="stat-card">
            <span>Total membres global</span>
            <strong>{{ total_members_all_time }}</strong>
            <p>Nombre total de membres enregistrés</p>
        </div>

        <div class="stat-card">
            <span>Membres créés période</span>
            <strong>{{ total_created_members }}</strong>
            <p>Membres visibles selon les filtres</p>
        </div>

        <div class="stat-card">
            <span>Membres ayant payé</span>
            <strong>{{ total_paid_members }}</strong>
            <p>Au moins un paiement validé</p>
        </div>

        <div class="stat-card">
            <span>Membres non payés</span>
            <strong>{{ total_unpaid_members }}</strong>
            <p>Aucun paiement validé</p>
        </div>

        <div class="stat-card">
            <span>Montant total des paiements</span>
            <strong>{{ total_payments_amount }}</strong>
            <p>Somme payée par les membres de la période</p>
        </div>
    </div>

    <div class="card">
        <div class="toolbar">
            <div>
                <h2 class="section-title" style="margin-bottom: 6px;">Filtres globaux</h2>
                <div class="muted">Filtrer les membres par date de création puis par statut de paiement.</div>
            </div>
        </div>

        <form method="get">
            <div class="filters-wrap">
                <div class="filters-grid">
                    <div class="field">
                        <label for="start_date">Date début</label>
                        <input type="date" id="start_date" name="start_date" value="{{ start_date }}">
                    </div>

                    <div class="field">
                        <label for="end_date">Date fin</label>
                        <input type="date" id="end_date" name="end_date" value="{{ end_date }}">
                    </div>

                    <div class="field">
                        <label for="payment_status">Statut de paiement</label>
                        <select id="payment_status" name="payment_status">
                            <option value="all" {% if payment_status == 'all' %}selected{% endif %}>Tous</option>
                            <option value="paid" {% if payment_status == 'paid' %}selected{% endif %}>Ont payé</option>
                            <option value="unpaid" {% if payment_status == 'unpaid' %}selected{% endif %}>N’ont pas payé</option>
                        </select>
                    </div>
                </div>

                <div class="filter-actions">
                    <button type="submit" class="btn btn-primary">Appliquer les filtres</button>
                    <a href="/admins/admins/performance/" class="btn btn-light">Réinitialiser</a>
                </div>
            </div>
        </form>
    </div>

    <div class="card table-card">
        <div class="table-head">
            <div class="toolbar">
                <div>
                    <h2 class="section-title" style="margin-bottom: 6px;">Résumé par administrateur</h2>
                    <div class="muted">
                        Vue synthétique des réalisations de chaque admin sur la période choisie.
                    </div>
                </div>

                <div class="export-actions">
                    <a href="/admins/admins/performance/admins-summary/export/?start_date={{ start_date }}&end_date={{ end_date }}"
                       class="btn btn-dark">
                        Télécharger le résumé des admins
                    </a>
                </div>
            </div>
        </div>

        {% if admins_summary_data %}
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Administrateur</th>
                            <th>Email</th>
                            <th>Rôle</th>
                            <th>Membres créés</th>
                            <th>Ont payé</th>
                            <th>N’ont pas payé</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in admins_summary_data %}
                            <tr class="admin-row {% if forloop.counter > 5 %}hidden-row extra-admin-row{% endif %}">
                                <td>
                                    <div class="admin-name">{{ item.admin.last_name }} {{ item.admin.first_name }}</div>
                                    <div class="admin-sub">NIM : {{ item.admin.nim }}</div>
                                </td>
                                <td>{{ item.admin.email }}</td>
                                <td>{{ item.admin.role }}</td>
                                <td><strong>{{ item.created_count }}</strong></td>
                                <td><span class="badge badge-paid">{{ item.paid_count }}</span></td>
                                <td><span class="badge badge-unpaid">{{ item.unpaid_count }}</span></td>
                                <td>
                                    <a href="/admins/admins/{{ item.admin.id }}/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=all"
                                       class="btn btn-outline">
                                        Voir détail
                                    </a>
                                </td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>

            {% if admins_summary_data|length > 5 %}
                <div class="see-more-wrap">
                    <button type="button" class="btn toggle-btn" id="toggle-admins-btn" onclick="toggleRows('extra-admin-row', 'toggle-admins-btn', 'Voir plus d’admins', 'Voir moins')">
                        Voir plus d’admins
                    </button>
                </div>
            {% endif %}
        {% else %}
            <div class="empty-state">
                Aucun administrateur trouvé.
            </div>
        {% endif %}
    </div>

    <div class="card">
        <div class="toolbar">
            <div>
                <h2 class="section-title" style="margin-bottom: 6px;">Export Excel global</h2>
                <div class="muted">Télécharger la vue filtrée actuelle avec l’admin créateur et le montant payé.</div>
            </div>

            <div class="export-actions">
                <a href="/admins/admins/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=all"
                   class="btn btn-dark">
                    Exporter tout
                </a>

                <a href="/admins/admins/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=paid"
                   class="btn btn-primary">
                    Exporter les payés
                </a>

                <a href="/admins/admins/performance/export/?start_date={{ start_date }}&end_date={{ end_date }}&payment_status=unpaid"
                   class="btn btn-outline">
                    Exporter les non payés
                </a>
            </div>
        </div>
    </div>

    <div class="card table-card">
        <div class="table-head">
            <h2 class="section-title" style="margin-bottom: 6px;">Tableau global des membres créés</h2>
            <div class="muted">
                Chaque ligne affiche le membre, son paiement total et l’administrateur qui l’a créé.
            </div>
        </div>

        {% if members %}
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>NIM membre</th>
                            <th>Membre</th>
                            <th>Téléphone</th>
                            <th>Ville</th>
                            <th>Date de création</th>
                            <th>Statut paiement</th>
                            <th>Montant total payé</th>
                            <th>Admin créateur</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for member in members %}
                            <tr class="member-row {% if forloop.counter > 8 %}hidden-row extra-member-row{% endif %}">
                                <td><strong>{{ member.nim }}</strong></td>
                                <td>
                                    <div class="member-name">{{ member.last_name }} {{ member.first_name }}</div>
                                    <div class="member-sub">
                                        Pièce : {{ member.id_card_type }}
                                        {% if member.id_card_number %}• {{ member.id_card_number }}{% endif %}
                                    </div>
                                </td>
                                <td>{{ member.phone|default:"Non renseigné" }}</td>
                                <td>{{ member.city|default:"Non renseignée" }}</td>
                                <td>{{ member.created_at|date:"d/m/Y à H:i" }}</td>
                                <td>
                                    {% if member.has_paid %}
                                        <span class="badge badge-paid">A payé</span>
                                    {% else %}
                                        <span class="badge badge-unpaid">N’a pas payé</span>
                                    {% endif %}
                                </td>
                                <td class="money">{{ member.total_paid_amount|default:0 }}</td>
                                <td>
                                    {% if member.created_by %}
                                        <div class="admin-name">{{ member.created_by.last_name }} {{ member.created_by.first_name }}</div>
                                        <div class="admin-sub">{{ member.created_by.email }}</div>
                                    {% else %}
                                        <span class="muted">Non défini</span>
                                    {% endif %}
                                </td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>

            {% if members|length > 8 %}
                <div class="see-more-wrap">
                    <button type="button" class="btn toggle-btn" id="toggle-members-btn" onclick="toggleRows('extra-member-row', 'toggle-members-btn', 'Voir plus de membres', 'Voir moins')">
                        Voir plus de membres
                    </button>
                </div>
            {% endif %}
        {% else %}
            <div class="empty-state">
                Aucun membre trouvé pour les filtres sélectionnés.
            </div>
        {% endif %}
    </div>
</div>

<script>
    function toggleRows(rowClass, buttonId, expandText, collapseText) {
        const rows = document.querySelectorAll('.' + rowClass);
        const button = document.getElementById(buttonId);

        if (!rows.length || !button) return;

        const isHidden = rows[0].classList.contains('hidden-row');

        rows.forEach(row => {
            if (isHidden) {
                row.classList.remove('hidden-row');
            } else {
                row.classList.add('hidden-row');
            }
        });

        button.textContent = isHidden ? collapseText : expandText;
    }
</script>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des publications</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: #111827;
        }

        .page {
            max-width: 1100px;
            margin: 35px auto;
            padding: 20px;
        }

        .topbar {
            background: white;
            border-radius: 22px;
            padding: 26px 30px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
            margin-bottom: 25px;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 34px;
            color: #111827;
        }

        .topbar p {
            margin: 0;
            color: #6b7280;
            line-height: 1.6;
        }

        .top-actions {
            margin-top: 18px;
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .btn {
            display: inline-block;
            text-decoration: none;
            text-align: center;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 15px;
            border: none;
            cursor: pointer;
        }

        .btn-blue {
            background: #2563eb;
            color: white;
        }

        .btn-dark {
            background: #374151;
            color: white;
        }

        .btn-green {
            background: #16a34a;
            color: white;
        }

        .btn-orange {
            background: #ea580c;
            color: white;
        }

        .btn-red {
            background: #dc2626;
            color: white;
        }

        .posts-list {
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .post-card {
            background: white;
            border-radius: 22px;
            overflow: hidden;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        .post-image img {
            width: 100%;
            height: 280px;
            object-fit: cover;
            display: block;
        }

        .post-body {
            padding: 22px;
        }

        .post-title {
            margin: 0 0 10px 0;
            font-size: 28px;
            color: #111827;
        }

        .post-meta {
            font-size: 14px;
            color: #6b7280;
            margin-bottom: 14px;
            line-height: 1.6;
        }

        .post-content {
            font-size: 16px;
            color: #374151;
            line-height: 1.8;
            white-space: pre-line;
        }

        .video-link {
            margin-top: 16px;
            padding: 14px 16px;
            background: #f9fafb;
            border-radius: 14px;
            border: 1px solid #e5e7eb;
        }

        .video-link a {
            color: #dc2626;
            font-weight: bold;
            text-decoration: none;
        }

        .post-actions {
            margin-top: 18px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .empty-box {
            background: white;
            border-radius: 22px;
            padding: 40px 24px;
            text-align: center;
            color: #6b7280;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        .empty-box h2 {
            margin-top: 0;
            color: #111827;
        }

        .delete-form {
            display: inline;
        }

        @media (max-width: 768px) {
            .page {
                padding: 14px;
                margin: 20px auto;
            }

            .topbar {
                padding: 22px 18px;
            }

            .topbar h1 {
                font-size: 28px;
            }

            .post-title {
                font-size: 23px;
            }

            .post-image img {
                height: 220px;
            }

            .top-actions,
            .post-actions {
                flex-direction: column;
            }

            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>

<div class="page">
    <div class="topbar">
        <h1>Liste des publications</h1>
        <p>Gérez ici toutes les informations publiées pour les membres.</p>

        <div class="top-actions">
            <a href="/admins/info-posts/create/" class="btn btn-blue">➕ Créer un post</a>
            <a href="/admins/admins-hub/" class="btn btn-dark">← Retour</a>
        </div>
    </div>

    {% if posts %}
        <div class="posts-list">
            {% for post in posts %}
                <div class="post-card">
                    {% if post.image %}
                        <div class="post-image">
                            <img src="{{ post.image.url }}" alt="{{ post.title }}">
                        </div>
                    {% endif %}

                    <div class="post-body">
                        <h2 class="post-title">{{ post.title }}</h2>

                        <div class="post-meta">
                            Publié le
                            {% if post.published_at %}
                                {{ post.published_at|date:"d/m/Y à H:i" }}
                            {% else %}
                                {{ post.created_at|date:"d/m/Y à H:i" }}
                            {% endif %}
                            {% if post.created_by %}
                                • par {{ post.created_by.first_name }} {{ post.created_by.last_name }}
                            {% endif %}
                        </div>

                        <div class="post-content">{{ post.content }}</div>

                        {% if post.video_url %}
                            <div class="video-link">
                                <a href="{{ post.video_url }}" target="_blank">▶ Voir la vidéo sur YouTube</a>
                            </div>
                        {% endif %}

                        <div class="post-actions">
                            <a href="/admins/info-posts/{{ post.id }}/edit/" class="btn btn-orange">Modifier</a>

                            <form method="POST" action="/admins/info-posts/{{ post.id }}/delete/" class="delete-form" onsubmit="return confirm('Supprimer ce post ?');">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-red">Supprimer</button>
                            </form>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="empty-box">
            <h2>Aucun post disponible</h2>
            <p>Commence par publier une première information pour les membres.</p>
        </div>
    {% endif %}
</div>

</body>
</html>




<!DOCTYPE html>
<html lang="fr">
<head>

    <meta name="robots" content="noindex, nofollow">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion Admin</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .login-container {
            width: 100%;
            max-width: 420px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
            padding: 35px 30px;
        }

        .login-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .login-header .icon {
            font-size: 50px;
            margin-bottom: 10px;
        }

        .login-header h2 {
            margin: 0;
            font-size: 30px;
            color: #111827;
        }

        .login-header p {
            margin-top: 8px;
            color: #6b7280;
            font-size: 15px;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #374151;
            font-weight: bold;
            font-size: 15px;
        }

        input {
            width: 100%;
            padding: 14px 15px;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            outline: none;
            font-size: 15px;
            transition: 0.3s;
        }

        input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.12);
        }

        .login-btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 12px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            margin-top: 10px;
        }

        .login-btn:hover {
            background: #1d4ed8;
        }

        .footer-text {
            text-align: center;
            margin-top: 20px;
            color: #6b7280;
            font-size: 14px;
        }

        @media (max-width: 500px) {
            .login-container {
                margin: 20px;
                padding: 28px 22px;
            }

            .login-header h2 {
                font-size: 25px;
            }
        }
    </style>
</head>
<body>

    <div class="login-container">
        <div class="login-header">
            <div class="icon">🔐</div>
            <h2>Connexion Admin</h2>
            <p>Accédez à votre espace d’administration</p>
        </div>

        <form method="POST">
            {% csrf_token %}

            <div class="form-group">
                <label for="email">Email</label>
                <input id="email" type="email" name="email" placeholder="Entrez votre email" required>
            </div>

            <div class="form-group">
                <label for="password">Mot de passe</label>
                <input id="password" type="password" name="password" placeholder="Entrez votre mot de passe" required>
            </div>

            <button type="submit" class="login-btn">Se connecter</button>
        </form>

        <div class="footer-text">
            Interface sécurisée d’administration
        </div>
    </div>

</body>
</html>





<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assistance</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
        }

        .page {
            padding: 20px;
        }

        .card {
            background: white;
            border-radius: 16px;
            padding: 22px 18px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        }

        h1 {
            margin-top: 0;
            font-size: 22px;
            color: #111827;
            text-align: center;
        }

        .subtitle {
            text-align: center;
            font-size: 14px;
            color: #6b7280;
            margin-top: 8px;
            margin-bottom: 20px;
        }

        .actions {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .action-btn {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px;
            border-radius: 14px;
            text-decoration: none;
            color: white;
            font-weight: bold;
            font-size: 15px;
        }

        .action-btn svg {
            width: 24px;
            height: 24px;
        }

        /* Couleurs */
        .call {
            background: #2563eb;
        }

        .whatsapp {
            background: #16a34a;
        }

        .email {
            background: #ea580c;
        }

        .footer {
            margin-top: 18px;
            text-align: center;
            font-size: 13px;
            color: #6b7280;
            line-height: 1.6;
        }

        .action-btn span {
            flex: 1;
        }

    </style>
</head>
<body>

<div class="page">
    <div class="card">

        <h1>Assistance</h1>
        <div class="subtitle">
            Nous sommes disponibles pour vous aider en cas de besoin.
        </div>

        <div class="actions">

            <!-- Appel -->
            <a href="tel:+2290160212109" class="action-btn call">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                        d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                </svg>
                <span>Appeler</span>
            </a>

            <!-- WhatsApp -->
            <a href="https://wa.me/2290160212109" class="action-btn whatsapp" target="_blank">
                <svg viewBox="0 0 24 24" fill="white">
                    <path d="M17.6 6.32C16.87 5.58 15.99 5 15.03 4.6C14.07 4.2 13.04 4 12 4C10.61 4 9.24 4.37 8.04 5.06C6.83 5.76 5.83 6.76 5.14 7.96C4.44 9.17 4.07 10.53 4.07 11.92C4.07 13.31 4.43 14.68 5.12 15.89L4 20L8.2 18.9C9.36 19.55 10.66 19.89 11.99 19.9C14.1 19.9 16.12 19.07 17.62 17.58C19.12 16.1 19.97 14.08 19.99 11.97C19.98 10.92 19.77 9.88 19.36 8.91C18.95 7.94 18.35 7.06 17.6 6.32Z"/>
                </svg>
                <span>WhatsApp</span>
            </a>

            <!-- Email -->
            <a href="mailto:contact@fondactionsarl.com" class="action-btn email">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="white">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                        d="M16.5 12a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm0 0c0 1.657 1.007 3 2.25 3S21 13.657 21 12a9 9 0 1 0-2.636 6.364M16.5 12V8.25" />
                </svg>
                <span>Envoyer un email</span>
            </a>

        </div>

        <div class="footer">
            Notre équipe vous répondra dans les plus brefs délais.
        </div>

    </div>
</div>

</body>
</html>


{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Carte membre</title>

    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #eee;
            color: #111827;
        }

        body {
            padding-top: 90px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
            display: flex;
            align-items: center;
            margin-left: 0px;
            margin-right: 0px;
        }

        .header-logo img {
            height: 85px;
            width: auto;
            object-fit: contain;
            transform: translateX(-18px);
        }

        .header-nim {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            background: #f1f5f9;
            padding: 8px 12px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            line-height: 1.2;
        }

        .nim-label {
            font-size: 10px;
            color: #6b7280;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .nim-value {
            font-size: 13px;
            font-weight: bold;
            color: #111827;
        }

        .page {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 35px;
            padding: 20px 16px 0;
        }

        .top-actions {
            width: 1000px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .top-actions a,
        .top-actions button {
            text-decoration: none;
            border: none;
            background: #2563eb;
            color: white;
            padding: 12px 18px;
            border-radius: 10px;
            font-weight: bold;
            cursor: pointer;
            font-size: 15px;
        }

        .top-actions a.secondary {
            background: #374151;
        }

        .capture-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 35px;
            background: white;
            padding: 20px;
            border-radius: 20px;
        }

        .card {
            width: 1000px;
            height: 600px;
            position: relative;
            background: url("{% static 'card-bg.png' %}") no-repeat center;
            background-size: cover;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        /* PHOTO */
        .photo {
            position: absolute;
            top: 200px;
            left: 180px;
            width: 200px;
            height: 250px;
            border-radius: 20px;
            overflow: hidden;
            border: 4px solid #f2c300;
        }

        .photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* NIM */
        .nim {
            position: absolute;
            top: 140px;
            left: 593px;
            font-size: 22px;
            font-weight: bold;
            background: #f7d73d;
            padding: 10px 20px;
            border-radius: 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }

        /* INFOS */
        .info {
            position: absolute;
            top: 200px;
            left: 420px;
            font-size: 18px;
            line-height: 32px;
        }

        .info strong {
            font-weight: bold;
        }

        /* SIGNATURE */
        .signature {
            position: absolute;
            bottom: 70px;
            left: 460px;
        }

        .signature img {
            width: 80px;
        }

        /* EXPIRATION */
        .expire {
            position: absolute;
            bottom: 70px;
            right: 155px;
            font-weight: bold;
            font-size: 16px;
            background: #1f8f3a;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        /* ===================== */
        /* VERSO */
        /* ===================== */

        .card-back {
            width: 1000px;
            height: 600px;
            position: relative;
            background: url("{% static 'card-back-bg.png' %}") no-repeat center;
            background-size: cover;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        .contacts {
            position: absolute;
            top: 220px;
            left: 510px;
            font-size: 24px;
            line-height: 48px;
            color: #222;
            font-weight: 500;
        }

        .footer-text {
            position: absolute;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%);
            width: 78%;
            text-align: center;
            font-size: 21px;
            line-height: 32px;
            color: #333;
            font-weight: 500;
        }

        .footer-nav {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            border-top: 1px solid #e5e7eb;
            padding: 10px 8px 14px;
        }

        .footer-nav-inner {
            max-width: 500px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 4px;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 5px;
            color: #6b7280;
            padding: 8px 3px;
            border-radius: 14px;
            min-height: 62px;
            text-align: center;
            overflow: hidden;
        }

        .nav-item.active {
            background: #eaf2ff;
            color: #2563eb;
        }

        .nav-item svg {
            width: 22px;
            height: 22px;
            flex-shrink: 0;
        }

        .nav-label {
            font-size: 10px;
            font-weight: 600;
            line-height: 1.1;
            word-break: break-word;
            overflow-wrap: break-word;
            max-width: 100%;
        }

        @media print {
            body {
                background: white;
                padding: 0;
            }

            .header,
            .footer-nav,
            .top-actions {
                display: none;
            }

            .page {
                gap: 20px;
                padding: 0;
            }

            .capture-area {
                background: transparent;
                padding: 0;
                border-radius: 0;
            }

            .card,
            .card-back {
                box-shadow: none;
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>

<header class="header">
    <div class="header-logo">
        <img src="/static/images/logo.png" alt="FondAction Logo">
    </div>

    <div class="header-nim">
        <span class="nim-label">NIM</span>
        <span class="nim-value">{{ member.nim }}</span>
    </div>
</header>

<div class="page">

    <div class="top-actions">
        <a href="/admins/member-space/" class="secondary">Retour espace membre</a>
        <button onclick="downloadCardPDF()">Télécharger PDF</button>
    </div>

    <div class="capture-area" id="capture-area">

        <!-- RECTO -->
        <div class="card">

            <div class="photo">
                {% if member.photo %}
                    <img src="{{ member.photo.url }}">
                {% endif %}
            </div>

            <div class="nim">
                NIM : {{ member.nim }}
            </div>

            <div class="info">
                <strong>Nom :</strong> {{ member.last_name }}<br>
                <strong>Prénom :</strong> {{ member.first_name }}<br>
                <strong>Date de naissance :</strong> {{ member.birth_date|date:"d/m/Y" }}<br>
                <strong>Lieu de naissance :</strong> {{ member.birth_place }}<br>
                <strong>Département :</strong> {{ member.department }}<br>
                <strong>Commune :</strong> {{ member.commune }}<br>
                <strong>Ville :</strong> {{ member.city }}<br>
                <strong>Quartier :</strong> {{ member.district }}
            </div>

            <div class="signature">
                {% if member.signature %}
                    <img src="{{ member.signature.url }}">
                {% endif %}
            </div>

            <div class="expire">
                Expire : 31/12/2031
            </div>

        </div>

        <!-- VERSO -->
        <div class="card-back">

            <div class="contacts">
                <div>📞 +2290160212109</div>
                <div>📧 contact@fondactionsarl.com</div>
                <div>🌐 www.foncdactionsarl.com</div>
            </div>

            <div class="footer-text">
                Cette pièce donne droit accès aux propriétés de la société FondAction SARL.
            </div>

        </div>

    </div>

</div>

<nav class="footer-nav">
    <div class="footer-nav-inner">
        <a href="/admins/member-space/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
            </svg>
            <div class="nav-label">Accueil</div>
        </a>

        <a href="/admins/member-card/" class="nav-item active">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
            </svg>
            <div class="nav-label">Carte</div>
        </a>

        <a href="/admins/member-infos/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
            </svg>
            <div class="nav-label">Infos</div>
        </a>

        <a href="/admins/member-profile/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Profil</div>
        </a>

        <a href="/admins/member-settings/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Paramètres</div>
        </a>
    </div>
</nav>

<script src="{% static 'js/html2canvas.min.js' %}"></script>
<script src="{% static 'js/jspdf.umd.min.js' %}"></script>

<script>
console.log("script principal chargé ✅");

async function waitForImages(container) {
    const images = container.querySelectorAll('img');
    const promises = [];

    images.forEach((img, index) => {
        if (img.complete) {
            return;
        }

        promises.push(new Promise((resolve) => {
            img.onload = () => {
                console.log("image chargée ✅", index, img.src);
                resolve();
            };
            img.onerror = () => {
                console.log("image erreur ⚠️", index, img.src);
                resolve();
            };
        }));
    });

    await Promise.all(promises);
}

window.downloadCardPDF = async function () {
    try {
        console.log("downloadCardPDF lancé ✅");
        console.log("window.jspdf =", window.jspdf);
        console.log("html2canvas =", typeof html2canvas);

        const { jsPDF } = window.jspdf;
        const captureArea = document.getElementById('capture-area');

        console.log("1. avant waitForImages");
        await waitForImages(captureArea);
        console.log("2. après waitForImages");

        const canvas = await html2canvas(captureArea, {
            scale: 1.5,
            useCORS: true,
            backgroundColor: "#ffffff",
            logging: true
        });

        console.log("3. canvas généré ✅");

        const imgData = canvas.toDataURL('image/png');
        console.log("4. image data générée ✅");

        const pdf = new jsPDF('p', 'mm', 'a4');
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();

        const imgWidth = pageWidth - 10;
        const imgHeight = (canvas.height * imgWidth) / canvas.width;

        let heightLeft = imgHeight;
        let position = 5;

        pdf.addImage(imgData, 'PNG', 5, position, imgWidth, imgHeight);
        console.log("5. première page ajoutée ✅");

        heightLeft -= (pageHeight - 10);

        while (heightLeft > 0) {
            position = heightLeft - imgHeight + 5;
            pdf.addPage();
            pdf.addImage(imgData, 'PNG', 5, position, imgWidth, imgHeight);
            heightLeft -= (pageHeight - 10);
            console.log("6. page supplémentaire ajoutée ✅");
        }

        pdf.save('carte-membre.pdf');
        console.log("7. PDF sauvegardé ✅");

    } catch (error) {
        console.error("Erreur downloadCardPDF ❌", error);
        alert("Erreur JS, regarde la console");
    }
};

console.log("downloadCardPDF =", typeof window.downloadCardPDF);
</script>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Changer le PIN</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #ffffff; /* 👉 fond blanc */
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 420px;
            background: white;
            border-radius: 20px;
            padding: 35px 30px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        }

        .header {
            text-align: center;
            margin-bottom: 25px;
        }

        /* 👉 CENTRAGE + STYLE ICÔNE */
        .icon {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 18px;
        }

        .icon svg {
            width: 42px;
            height: 42px;
            color: #2563eb; /* 👉 belle couleur bleue pro */
        }

        .header h1 {
            margin: 0;
            font-size: 24px;
            color: #111827;
        }

        .header p {
            margin-top: 8px;
            font-size: 14px;
            color: #6b7280;
        }

        .warning {
            background: #fef3c7;
            color: #92400e;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 18px;
            font-size: 13px;
            text-align: center;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 14px;
            border-radius: 12px;
            border: 1px solid #d1d5db;
            font-size: 15px;
            outline: none;
            transition: 0.3s;
        }

        input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37,99,235,0.1);
        }

        .btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 12px;
            background: #16a34a;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn:hover {
            background: #15803d;
        }

        .footer {
            margin-top: 15px;
            text-align: center;
            font-size: 12px;
            color: #9ca3af;
        }

        @media (max-width: 500px) {
            .container {
                margin: 20px;
                padding: 28px 22px;
            }
        }
    </style>
</head>
<body>

    <div class="container">

        <!-- 👉 ICÔNE CENTRÉE -->
        <div class="icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.91 11.12C20.91 16.01 17.36 20.59 12.51 21.93C12.18 22.02 11.82 22.02 11.49 21.93C6.63996 20.59 3.08997 16.01 3.08997 11.12V6.72997C3.08997 5.90997 3.70998 4.97998 4.47998 4.66998L10.05 2.39001C11.3 1.88001 12.71 1.88001 13.96 2.39001L19.53 4.66998C20.29 4.97998 20.92 5.90997 20.92 6.72997L20.91 11.12Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                <path d="M12 12.5C13.1046 12.5 14 11.6046 14 10.5C14 9.39543 13.1046 8.5 12 8.5C10.8954 8.5 10 9.39543 10 10.5C10 11.6046 10.8954 12.5 12 12.5Z" stroke="currentColor" stroke-width="1.5"></path>
                <path d="M12 12.5V15.5" stroke="currentColor" stroke-width="1.5"></path>
            </svg>
        </div>

        <div class="header">
            <h1>Changer votre PIN</h1>
            <p>Sécurisez votre compte avec un nouveau code personnel</p>
        </div>

        <div class="warning">
            ⚠️ Votre code PIN est strictement personnel. Ne le partagez avec personne.
        </div>

        <form method="POST">
            {% csrf_token %}

            <div class="form-group">
                <label>Nouveau PIN (5 chiffres)</label>
                <input type="password" name="new_pin" maxlength="5" placeholder="•••••" required>
            </div>

            <div class="form-group">
                <label>Confirmer le nouveau PIN</label>
                <input type="password" name="confirm_pin" maxlength="5" placeholder="•••••" required>
            </div>

            <button type="submit" class="btn">Valider</button>
        </form>

        

    </div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historique de création des membres</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            max-width: 1200px;
            margin: 30px auto;
            padding: 20px;
        }

        .header {
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            color: white;
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 20px;
        }

        .header h1 {
            margin: 0;
            font-size: 32px;
        }

        .actions {
            margin: 20px 0;
        }

        .btn {
            display: inline-block;
            padding: 12px 18px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: bold;
            background: #374151;
            color: white;
        }

        .table-card {
            background: white;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 14px;
            text-align: left;
            border-bottom: 1px solid #e5e7eb;
        }

        th {
            background: #f9fafb;
            color: #111827;
            font-size: 15px;
        }

        td {
            color: #374151;
        }

        .badge {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            background: #dbeafe;
            color: #1d4ed8;
            font-size: 13px;
            font-weight: bold;
        }

        .empty {
            text-align: center;
            padding: 30px;
            color: #6b7280;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="page">

    <div class="header">
        <h1>🕘 Historique de création des membres</h1>
        {% if role == 'super_admin' %}
            <p>Vue globale de toutes les créations de membres.</p>
        {% else %}
            <p>Voici les membres que vous avez enregistrés.</p>
        {% endif %}
    </div>

    <div class="actions">
        <a href="/admins/dashboard/" class="btn">⬅ Retour dashboard</a>
    </div>

    <div class="table-card">
        <table>
            <thead>
                <tr>
                    <th>NIM</th>
                    <th>Nom</th>
                    <th>Prénom</th>
                    <th>Date</th>
                    <th>Heure</th>
                    {% if role == 'super_admin' %}
                        <th>Créé par</th>
                    {% endif %}
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for member in members %}
                <tr>
                    <td><span class="badge">{{ member.nim }}</span></td>
                    <td>{{ member.last_name }}</td>
                    <td>{{ member.first_name }}</td>
                    <td>{{ member.created_at|date:"d/m/Y" }}</td>
                    <td>{{ member.created_at|date:"H:i" }}</td>
                    {% if role == 'super_admin' %}
                        <td>
                            {% if member.created_by %}
                                {{ member.created_by.email }}
                            {% else %}
                                —
                            {% endif %}
                        </td>
                    {% endif %}
                    <td>
                        <a href="/admins/members/{{ member.id }}/">Voir détail</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="{% if role == 'super_admin' %}7{% else %}6{% endif %}" class="empty">
                        Aucun historique trouvé
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Détail du membre</title>

    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg-1: #f8fafc;
            --bg-2: #eef2f7;
            --card: rgba(255, 255, 255, 0.96);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e5e7eb;
            --line-soft: #edf2f7;
            --blue: #2563eb;
            --blue-soft: #dbeafe;
            --green: #16a34a;
            --green-soft: #dcfce7;
            --red: #dc2626;
            --red-soft: #fee2e2;
            --orange: #d97706;
            --orange-soft: #fef3c7;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --shadow-soft: 0 10px 24px rgba(15, 23, 42, 0.06);
            --radius-xl: 24px;
            --radius-lg: 18px;
            --radius-md: 14px;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.05), transparent 30%),
                linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 100%);
            color: var(--text);
        }

        .page {
            max-width: 1180px;
            margin: 28px auto 40px;
            padding: 20px;
        }

        .topbar {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.6);
            border-radius: 28px;
            padding: 28px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
            backdrop-filter: blur(10px);
        }

        .topbar-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 18px;
            flex-wrap: wrap;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 36px;
            color: var(--text);
            letter-spacing: -0.5px;
        }

        .topbar p {
            margin: 0;
            color: var(--muted);
            line-height: 1.7;
            max-width: 700px;
        }

        .topbar-links {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .topbar-links a {
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
            padding: 12px 16px;
            border-radius: 12px;
            transition: 0.2s ease;
        }

        .topbar-links a:hover {
            transform: translateY(-1px);
        }

        .btn-back {
            background: #e5e7eb;
            color: var(--text);
        }

        .btn-list {
            background: var(--blue);
            color: white;
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.18);
        }

        .member-hero {
            margin-top: 20px;
            display: flex;
            align-items: center;
            gap: 18px;
            flex-wrap: wrap;
            padding-top: 18px;
            border-top: 1px solid var(--line-soft);
        }

        .hero-avatar {
            width: 86px;
            height: 86px;
            border-radius: 22px;
            overflow: hidden;
            border: 4px solid #fff;
            box-shadow: var(--shadow-soft);
            background: #f3f4f6;
            flex-shrink: 0;
        }

        .hero-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hero-avatar-fallback {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            font-weight: bold;
            color: var(--blue);
            background: var(--blue-soft);
        }

        .hero-content {
            flex: 1;
            min-width: 220px;
        }

        .hero-name {
            margin: 0 0 8px 0;
            font-size: 28px;
            font-weight: bold;
            color: var(--text);
        }

        .hero-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 14px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: bold;
            border: 1px solid var(--line);
            background: #fff;
            color: #334155;
        }

        .nim-pill {
            background: var(--blue-soft);
            color: #1d4ed8;
            border-color: #bfdbfe;
        }

        .layout {
            display: grid;
            grid-template-columns: 1.2fr 0.95fr;
            gap: 22px;
            margin-bottom: 22px;
        }

        .card {
            background: var(--card);
            border-radius: var(--radius-xl);
            padding: 24px;
            box-shadow: var(--shadow);
            border: 1px solid rgba(255,255,255,0.65);
            backdrop-filter: blur(10px);
        }

        .card + .card {
            margin-top: 22px;
        }

        .card h3 {
            margin: 0 0 18px 0;
            font-size: 22px;
            color: var(--text);
            letter-spacing: -0.2px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--line-soft);
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }

        .info-item {
            background: #f8fafc;
            border: 1px solid var(--line-soft);
            border-radius: 16px;
            padding: 14px 15px;
            min-height: 78px;
        }

        .info-label {
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            color: var(--muted);
            margin-bottom: 8px;
        }

        .info-value {
            font-size: 15px;
            line-height: 1.6;
            color: #334155;
            word-break: break-word;
        }

        .info-item.full {
            grid-column: 1 / -1;
        }

        .status {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .status-active {
            background: var(--green-soft);
            color: #166534;
        }

        .status-suspended {
            background: var(--red-soft);
            color: #991b1b;
        }

        .status-inactive {
            background: #f3f4f6;
            color: #4b5563;
        }

        .status-locked {
            background: var(--orange-soft);
            color: #92400e;
        }

        .security-note {
            margin-top: 16px;
            padding: 16px;
            border-radius: 16px;
            background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
            color: #475569;
            line-height: 1.7;
            border: 1px solid var(--line);
        }

        .action-box {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-top: 18px;
        }

        .btn {
            text-decoration: none;
            display: inline-block;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
            transition: 0.2s ease;
        }

        .btn:hover {
            transform: translateY(-1px);
        }

        .btn-blue {
            background: var(--blue);
            color: white;
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.16);
        }

        .btn-red {
            background: var(--red);
            color: white;
            box-shadow: 0 10px 20px rgba(220, 38, 38, 0.14);
        }

        .btn-green {
            background: var(--green);
            color: white;
            box-shadow: 0 10px 20px rgba(22, 163, 74, 0.14);
        }

        .image-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px;
        }

        .image-box {
            background: #f8fafc;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 15px;
            text-align: center;
        }

        .image-box h4 {
            margin: 0 0 12px 0;
            font-size: 16px;
            color: #374151;
        }

        .image-box img {
            width: 100%;
            max-width: 220px;
            height: 220px;
            object-fit: cover;
            border-radius: 12px;
            border: 1px solid #dbe2ea;
            cursor: pointer;
            transition: transform 0.2s ease;
            background: white;
        }

        .image-box img:hover {
            transform: scale(1.02);
        }

        .view-photo-btn {
            display: inline-block;
            margin-top: 12px;
            padding: 9px 13px;
            border-radius: 10px;
            background: var(--blue);
            color: white;
            text-decoration: none;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
            border: none;
        }

        .empty-box {
            padding: 28px 14px;
            color: var(--muted);
            background: #f3f4f6;
            border-radius: 12px;
            line-height: 1.6;
        }

        .detail-card {
            background: var(--card);
            border-radius: 24px;
            padding: 24px;
            box-shadow: var(--shadow);
            border: 1px solid rgba(255,255,255,0.65);
        }

        .detail-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 14px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .detail-card h2 {
            margin: 0;
            color: var(--text);
            font-size: 24px;
            letter-spacing: -0.3px;
        }

        .detail-badge {
            padding: 10px 14px;
            border-radius: 999px;
            background: var(--blue-soft);
            color: #1d4ed8;
            font-weight: bold;
            font-size: 13px;
            border: 1px solid #bfdbfe;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
            border: 1px solid var(--line);
            border-radius: 18px;
            background: white;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 760px;
        }

        th, td {
            padding: 14px 16px;
            border-bottom: 1px solid var(--line);
            text-align: left;
            font-size: 14px;
            vertical-align: middle;
        }

        th {
            background: #f8fafc;
            color: var(--text);
            font-size: 13px;
            letter-spacing: 0.2px;
        }

        tr:last-child td {
            border-bottom: none;
        }

        td {
            color: #334155;
        }

        .tx-pill {
            display: inline-block;
            padding: 7px 11px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            background: #eff6ff;
            color: #1d4ed8;
        }

        .success {
            color: #166534;
        }

        .pending {
            color: #92400e;
        }

        .failed {
            color: #991b1b;
        }

        .photo-modal {
            display: none;
            position: fixed;
            z-index: 9999;
            inset: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.82);
            justify-content: center;
            align-items: center;
            padding: 30px;
        }

        .photo-modal img {
            max-width: 95%;
            max-height: 90vh;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
            background: white;
        }

        .photo-modal .close-btn {
            position: absolute;
            top: 20px;
            right: 28px;
            font-size: 34px;
            color: white;
            cursor: pointer;
            font-weight: bold;
        }

        @media (max-width: 980px) {
            .layout {
                grid-template-columns: 1fr;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }

            .image-grid {
                grid-template-columns: 1fr 1fr;
            }

            .topbar h1 {
                font-size: 30px;
            }

            .hero-name {
                font-size: 24px;
            }
        }

        @media (max-width: 680px) {
            .page {
                padding: 14px;
                margin: 18px auto 30px;
            }

            .topbar,
            .card,
            .detail-card {
                padding: 18px;
                border-radius: 20px;
            }

            .topbar-links {
                width: 100%;
            }

            .topbar-links a,
            .btn {
                width: 100%;
                text-align: center;
            }

            .image-grid {
                grid-template-columns: 1fr;
            }

            .hero-avatar {
                width: 76px;
                height: 76px;
            }

            .hero-name {
                font-size: 22px;
            }
        }
    </style>
</head>
<body>
    <div class="page">
        <div class="topbar">
            <div class="topbar-top">
                <div>
                    <h1>Détail du membre</h1>
                    <p>
                        Consultez les informations complètes du membre, ses documents d’identification,
                        son niveau de sécurité et son historique de transactions.
                    </p>
                </div>

                <div class="topbar-links">
                    <a href="/admins/members-hub/" class="btn-back">← Espace membres</a>
                    <a href="/admins/members/" class="btn-list">📋 Liste des membres</a>
                </div>
            </div>

            <div class="member-hero">
                <div class="hero-avatar">
                    {% if member.photo %}
                        <img src="{{ member.photo.url }}" alt="Photo du membre">
                    {% else %}
                        <div class="hero-avatar-fallback">
                            {{ member.last_name|default:"M"|slice:":1" }}
                        </div>
                    {% endif %}
                </div>

                <div class="hero-content">
                    <div class="hero-name">
                        {{ member.last_name|default:"—" }} {{ member.first_name|default:"—" }}
                    </div>

                    <div class="hero-meta">
                        <span class="hero-pill nim-pill">NIM : {{ member.nim }}</span>

                        {% if member.status == 'active' %}
                            <span class="hero-pill status-active">Actif</span>
                        {% elif member.status == 'suspended' %}
                            <span class="hero-pill status-suspended">Suspendu</span>
                        {% else %}
                            <span class="hero-pill status-inactive">Inactif</span>
                        {% endif %}

                        {% if member.phone %}
                            <span class="hero-pill">{{ member.phone }}</span>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>

        <div class="layout">
            <div>
                <div class="card">
                    <h3>Informations générales</h3>

                    <div class="info-grid">
                        <div class="info-item">
                            <div class="info-label">Nom</div>
                            <div class="info-value">{{ member.last_name|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Prénom</div>
                            <div class="info-value">{{ member.first_name|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Date de naissance</div>
                            <div class="info-value">{{ member.birth_date|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Lieu de naissance</div>
                            <div class="info-value">{{ member.birth_place|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Département</div>
                            <div class="info-value">{{ member.department|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Commune</div>
                            <div class="info-value">{{ member.commune|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Ville</div>
                            <div class="info-value">{{ member.city|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Quartier</div>
                            <div class="info-value">{{ member.district|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Téléphone</div>
                            <div class="info-value">{{ member.phone|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Type de pièce</div>
                            <div class="info-value">{{ member.id_card_type|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Numéro de pièce</div>
                            <div class="info-value">{{ member.id_card_number|default:"—" }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Date d’enregistrement</div>
                            <div class="info-value">{{ member.created_at|date:"d/m/Y à H:i" }}</div>
                        </div>

                        <div class="info-item full">
                            <div class="info-label">Créé par</div>
                            <div class="info-value">
                                {% if member.created_by %}
                                    {{ member.created_by.email }}
                                {% else %}
                                    —
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <h3>Personne à contacter</h3>

                    <div class="info-grid">
                        <div class="info-item">
                            <div class="info-label">Nom</div>
                            <div class="info-value">{{ member.emergency_last_name|default:"—" }}</div>
                        </div>
                      <div class="info-item">
                            <div class="info-label">Prénom</div>
                            <div class="info-value">{{ member.emergency_first_name|default:"—" }}</div>
                        </div>

                        <div class="info-item full">
                            <div class="info-label">Téléphone</div>
                            <div class="info-value">{{ member.emergency_phone|default:"—" }}</div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <h3>Sécurité du compte</h3>

                    <div class="info-grid">
                        <div class="info-item">
                            <div class="info-label">Tentatives PIN échouées</div>
                            <div class="info-value">{{ member.failed_pin_attempts }}</div>
                        </div>

                        <div class="info-item">
                            <div class="info-label">Compte bloqué</div>
                            <div class="info-value">
                                {% if member.is_locked %}
                                    <span class="status status-locked">Oui</span>
                                {% else %}
                                    <span class="status status-active">Non</span>
                                {% endif %}
                            </div>
                        </div>
                    </div>

                    <div class="security-note">
                        Utilise la réinitialisation du PIN si le membre a oublié son code
                        ou si son compte a été bloqué après plusieurs tentatives incorrectes.
                    </div>

                    <div class="action-box">
                        <a href="/admins/members/{{ member.id }}/edit/" class="btn btn-blue">
                            ✏️ Modifier le membre
                        </a>

                        <a href="/admins/members/{{ member.id }}/reset-pin/" class="btn btn-red">
                            🔑 Réinitialiser le PIN
                        </a>

                        {% if member.status == 'active' %}
                            <a href="/admins/members/{{ member.id }}/suspend/" class="btn btn-red">
                                ⛔ Suspendre le membre
                            </a>
                        {% else %}
                            <a href="/admins/members/{{ member.id }}/activate/" class="btn btn-green">
                                ✅ Réactiver le membre
                            </a>
                        {% endif %}
                    </div>
                </div>
            </div>

            <div>
                <div class="card">
                    <h3>Images & documents</h3>

                    <div class="image-grid">
                        <div class="image-box">
                            <h4>Photo du membre</h4>
                            {% if member.photo %}
                                <img src="{{ member.photo.url }}" alt="Photo membre" onclick="openPhotoModal('{{ member.photo.url }}')">
                                <button type="button" class="view-photo-btn" onclick="openPhotoModal('{{ member.photo.url }}')">
                                    Voir la photo
                                </button>
                            {% else %}
                                <div class="empty-box">Aucune photo</div>
                            {% endif %}
                        </div>

                        <div class="image-box">
                            <h4>Recto de pièce</h4>
                            {% if member.id_card_front %}
                                <img src="{{ member.id_card_front.url }}" alt="Recto pièce" onclick="openPhotoModal('{{ member.id_card_front.url }}')">
                                <button type="button" class="view-photo-btn" onclick="openPhotoModal('{{ member.id_card_front.url }}')">
                                    Voir le document
                                </button>
                            {% else %}
                                <div class="empty-box">Aucun recto</div>
                            {% endif %}
                        </div>

                        <div class="image-box">
                            <h4>Verso de pièce</h4>
                            {% if member.id_card_back %}
                                <img src="{{ member.id_card_back.url }}" alt="Verso pièce" onclick="openPhotoModal('{{ member.id_card_back.url }}')">
                                <button type="button" class="view-photo-btn" onclick="openPhotoModal('{{ member.id_card_back.url }}')">
                                    Voir le document
                                </button>
                            {% else %}
                                <div class="empty-box">Aucun verso</div>
                            {% endif %}
                        </div>

                        <div class="image-box">
                            <h4>Signature</h4>
                            {% if member.signature %}
                                <img src="{{ member.signature.url }}" alt="Signature" onclick="openPhotoModal('{{ member.signature.url }}')">
                                <button type="button" class="view-photo-btn" onclick="openPhotoModal('{{ member.signature.url }}')">
                                    Voir la signature
                                </button>
                            {% else %}
                                <div class="empty-box">Aucune signature</div>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="detail-card">
            <div class="detail-header">
                <h2>Historique des transactions</h2>
                <div class="detail-badge">
                    {% if transactions %}{{ transactions|length }} transaction{{ transactions|length|pluralize }}{% else %}0 transaction{% endif %}
                </div>
            </div>

            {% if transactions %}
                <div class="table-wrap">
                    <table>
                        <thead>
                            <tr>
                                <th>Reçu</th>
                                <th>Référence</th>
                                <th>Type</th>
                                <th>Montant</th>
                                <th>Statut</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for tx in transactions %}
                                <tr>
                                    <td>{{ tx.receipt_number|default:"—" }}</td>
                                    <td>{{ tx.reference }}</td>
                                    <td>
                                        <span class="tx-pill">{{ tx.transaction_type }}</span>
                                    </td>
                                    <td>{{ tx.amount }} FCFA</td>
                                    <td>
                                        {% if tx.status == 'success' %}
                                            <span class="status success">Succès</span>
                                        {% elif tx.status == 'pending' %}
                                            <span class="status pending">En attente</span>
                                        {% else %}
                                            <span class="status failed">Échoué</span>
                                        {% endif %}
                                    </td>
                                    <td>{{ tx.created_at|date:"d/m/Y H:i" }}</td>
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            {% else %}
                <div class="empty-box">Aucune transaction trouvée pour ce membre.</div>
            {% endif %}
        </div>
    </div>

    <div id="photoModal" class="photo-modal" onclick="closePhotoModal()">
        <span class="close-btn" onclick="closePhotoModal()">&times;</span>
        <img id="photoModalImg" src="" alt="Aperçu photo">
    </div>

    <script>
        function openPhotoModal(imageUrl) {
            const modal = document.getElementById('photoModal');
            const modalImg = document.getElementById('photoModalImg');
            modalImg.src = imageUrl;
            modal.style.display = 'flex';
        }

        function closePhotoModal() {
            const modal = document.getElementById('photoModal');
            const modalImg = document.getElementById('photoModalImg');
            modal.style.display = 'none';
            modalImg.src = '';
        }
    </script>
</body>
</html>  


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informations membres</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: #111827;
            scroll-behavior: smooth;
        }

        body {
            padding-top: 78px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
            display: flex;
            align-items: center;
            margin-left: 0px;
            margin-right: 0px;
        }

        .header-logo img {
            height: 85px;
            width: auto;
            object-fit: contain;
            transform: translateX(-18px);
        }

        .header-nim {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            background: #f1f5f9;
            padding: 8px 12px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            line-height: 1.2;
        }

        .nim-label {
            font-size: 10px;
            color: #6b7280;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .nim-value {
            font-size: 13px;
            font-weight: bold;
            color: #111827;
        }

        .page {
            max-width: 1100px;
            margin: 30px auto;
            padding: 20px;
        }

        .topbar {
            background: white;
            border-radius: 22px;
            padding: 28px 30px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
            margin-bottom: 25px;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 34px;
            color: #111827;
        }

        .topbar p {
            margin: 0;
            color: #6b7280;
            line-height: 1.6;
            font-size: 16px;
        }

        .top-actions {
            margin-top: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }

        .back-btn,
        .recent-btn {
            display: inline-block;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 15px;
            text-align: center;
        }

        .back-btn {
            background: #1f2937;
            color: white;
        }

        .recent-btn {
            background: #2563eb;
            color: white;
        }

        .posts-list {
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .post-card {
            background: white;
            border-radius: 22px;
            overflow: hidden;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
            scroll-margin-top: 95px;
        }

        .post-image img {
            width: 100%;
            height: 320px;
            object-fit: cover;
            display: block;
        }

        .post-body {
            padding: 24px;
        }

        .post-title {
            margin: 0 0 14px 0;
            font-size: 28px;
            color: #111827;
            word-wrap: break-word;
            overflow-wrap: break-word;
            word-break: break-word;
        }

        .post-meta {
            margin-bottom: 14px;
            font-size: 14px;
            color: #6b7280;
        }

        .post-content {
            font-size: 16px;
            color: #374151;
            line-height: 1.8;
            white-space: pre-line;
            word-wrap: break-word;
            overflow-wrap: break-word;
            word-break: break-word;
        }

        .post-video-box {
            margin-top: 20px;
            padding: 16px;
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
        }

        .post-video-text {
            margin: 0 0 12px 0;
            color: #4b5563;
            font-size: 15px;
        }

        .btn-youtube {
            display: inline-block;
            padding: 12px 18px;
            background: #ff0000;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            text-decoration: none;
            font-size: 15px;
        }

        .btn-youtube:hover {
            background: #cc0000;
        }

        .empty-box {
            background: white;
            border-radius: 22px;
            padding: 40px 24px;
            text-align: center;
            color: #6b7280;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }

        .empty-box h2 {
            margin-top: 0;
            color: #111827;
            font-size: 26px;
        }

        .empty-box p {
            margin: 10px 0 0 0;
            line-height: 1.7;
        }

        .footer-nav {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            border-top: 1px solid #e5e7eb;
            padding: 10px 8px 14px;
        }

        .footer-nav-inner {
            max-width: 500px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 4px;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 5px;
            color: #6b7280;
            padding: 8px 3px;
            border-radius: 14px;
            min-height: 62px;
            text-align: center;
            overflow: hidden;
        }

        .nav-item.active {
            background: #eaf2ff;
            color: #2563eb;
        }

        .nav-item svg {
            width: 22px;
            height: 22px;
            flex-shrink: 0;
        }

        .nav-label {
            font-size: 10px;
            font-weight: 600;
            line-height: 1.1;
            word-break: break-word;
            overflow-wrap: break-word;
            max-width: 100%;
        }

        @media (max-width: 768px) {
            .page {
                padding: 14px;
                margin: 20px auto;
            }

            .topbar {
                padding: 22px 18px;
            }

            .topbar h1 {
                font-size: 28px;
            }

            .post-title {
                font-size: 24px;
            }

            .post-body {
                padding: 18px;
            }

            .post-image img {
                height: 220px;
            }

            .back-btn,
            .recent-btn,
            .btn-youtube {
                width: 100%;
                text-align: center;
            }

            .top-actions {
                flex-direction: column;
                align-items: stretch;
            }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="header-logo">
            <img src="/static/images/logo.png" alt="FondAction Logo">
        </div>

        <div class="header-nim">
            <span class="nim-label">NIM</span>
            <span class="nim-value">{{ member.nim }}</span>
        </div>
    </header>

    <div class="page">
        <div class="topbar">
            <h1>Informations importantes</h1>
            <p>
                Retrouvez ici toutes les annonces, publications et informations partagées par l’administration.
                Ces contenus sont consultables par tous les membres.
            </p>

            <div class="top-actions">
                <a href="/admins/member-space/" class="back-btn">Retour</a>
                <a href="#latest-post" class="recent-btn">Récent</a>
            </div>
        </div>

        {% if posts %}
            <div class="posts-list">
                {% for post in posts %}
                    <div class="post-card" {% if forloop.first %}id="latest-post"{% endif %}>
                        {% if post.image %}
                            <div class="post-image">
                                <img src="{{ post.image.url }}" alt="{{ post.title }}">
                            </div>
                        {% endif %}

                        <div class="post-body">
                            <h2 class="post-title">{{ post.title }}</h2>

                            <div class="post-meta">
                                Publié le
                                {% if post.published_at %}
                                    {{ post.published_at|date:"d/m/Y à H:i" }}
                                {% else %}
                                    {{ post.created_at|date:"d/m/Y à H:i" }}
                                {% endif %}
                            </div>

                            <div class="post-content">
                                {{ post.content }}
                            </div>

                            {% if post.video_url %}
                                <div class="post-video-box">
                                    <p class="post-video-text">
                                        Une vidéo est associée à cette publication. Cliquez sur le bouton ci-dessous pour la regarder sur YouTube.
                                    </p>
                                    <a href="{{ post.video_url }}" target="_blank" class="btn-youtube">
                                        ▶ Regarder la vidéo sur YouTube
                                    </a>
                                </div>
                            {% endif %}
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="empty-box">
                <h2>Aucune information disponible</h2>
                <p>
                    Aucune publication n’a encore été ajoutée par l’administration pour le moment.
                </p>
            </div>
        {% endif %}
    </div>

    <nav class="footer-nav">
        <div class="footer-nav-inner">
            <a href="/admins/member-space/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>
                <div class="nav-label">Accueil</div>
            </a>

            <a href="/admins/member-card/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                </svg>
                <div class="nav-label">Carte</div>
            </a>

            <a href="/admins/member-infos/" class="nav-item active">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
                </svg>
                <div class="nav-label">Infos</div>
            </a>

            <a href="/admins/member-profile/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Profil</div>
            </a>

            <a href="/admins/member-settings/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Paramètres</div>
            </a>
        </div>
    </nav>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des membres</title>

    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.96);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --success: #16a34a;
            --danger: #dc2626;
            --warning: #d97706;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(14, 165, 233, 0.08), transparent 26%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
            color: var(--text);
        }

        .page {
            max-width: 1380px;
            margin: 30px auto;
            padding: 20px;
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #2563eb 100%);
            color: white;
            border-radius: 30px;
            padding: 30px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
        }

        .hero::after {
            content: "";
            position: absolute;
            top: -90px;
            right: -80px;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .hero small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.82;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }

        .hero h1 {
            margin: 0 0 10px 0;
            font-size: 36px;
            line-height: 1.15;
            position: relative;
            z-index: 1;
        }

        .hero p {
            margin: 0;
            max-width: 820px;
            line-height: 1.7;
            color: rgba(255,255,255,0.88);
            position: relative;
            z-index: 1;
        }

        .hero-actions {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 20px;
            position: relative;
            z-index: 1;
        }

        .hero-btn,
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 14px;
            border: none;
            cursor: pointer;
            transition: 0.2s ease;
        }

        .hero-btn:hover,
        .btn:hover,
        .btn-detail:hover {
            transform: translateY(-1px);
        }

        .hero-btn-light {
            background: white;
            color: #0f172a;
        }

        .hero-btn-outline {
            background: rgba(255,255,255,0.12);
            color: white;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .section-card {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: 26px;
            padding: 24px;
            box-shadow: var(--shadow);
            margin-bottom: 22px;
            backdrop-filter: blur(10px);
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }

        .section-head h2 {
            margin: 0 0 6px;
            font-size: 24px;
        }

        .section-head p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .search-form {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 16px;
            align-items: end;
        }

        .search-fields {
            display: grid;
            grid-template-columns: repeat(2, minmax(220px, 1fr));
            gap: 14px;
        }

        .field label {
            display: block;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #334155;
        }

        .field input {
            width: 100%;
            padding: 13px 14px;
            border-radius: 14px;
            border: 1px solid #cbd5e1;
            background: white;
            font-size: 14px;
            outline: none;
        }

        .field input:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
        }

        .search-actions,
        .table-actions {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
        }

        .btn-light {
            background: #e2e8f0;
            color: #0f172a;
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        .btn-success {
            background: var(--success);
            color: white;
        }

        .table-box {
            background: white;
            border-radius: 24px;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
            border: 1px solid var(--line);
            overflow: hidden;
        }

        .table-top {
            padding: 22px 22px 14px;
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
        }

        .table-top h3 {
            margin: 0 0 6px;
            font-size: 22px;
        }

        .table-top p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 1020px;
        }

        th {
            text-align: left;
            padding: 16px 18px;
            background: #f8fafc;
            font-size: 13px;
            color: #334155;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            border-bottom: 1px solid var(--line);
        }

        td {
            padding: 18px;
            border-top: 1px solid #eef2f7;
            font-size: 14px;
            color: #334155;
            vertical-align: middle;
        }

        tr:hover {
            background: #f8fbff;
        }

        .member-name {
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 4px;
        }

        .member-sub {
            color: var(--muted);
            font-size: 13px;
        }

        .nim {
            font-weight: bold;
            color: #0f172a;
        }

        .status {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .status-active {
            background: #dcfce7;
            color: #166534;
        }

        .status-suspended {
            background: #fee2e2;
            color: #991b1b;
        }

        .status-inactive {
            background: #f3f4f6;
            color: #4b5563;
        }

        .btn-detail {
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 10px 14px;
            border-radius: 12px;
            background: #eff6ff;
            color: #1d4ed8;
            font-size: 13px;
            font-weight: bold;
            transition: 0.2s ease;
        }

        .empty {
            text-align: center;
            padding: 28px;
            color: var(--muted);
        }

        @media (max-width: 980px) {
            .search-form {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 760px) {
            .page {
                padding: 14px;
            }

            .hero {
                padding: 24px 22px;
                border-radius: 24px;
            }

            .hero h1 {
                font-size: 28px;
            }

            .section-card {
                padding: 18px;
                border-radius: 22px;
            }

            .search-fields {
                grid-template-columns: 1fr;
            }

            .hero-actions,
            .search-actions,
            .table-actions {
                flex-direction: column;
            }

            .hero-btn,
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>

<div class="page">

    <div class="hero">
        <small>Administration • Gestion des membres</small>
        <h1>Liste des membres</h1>
        <p>
            Consultez les membres enregistrés, recherchez rapidement un dossier par NIM ou téléphone,
            puis accédez au détail complet de chaque profil avec une interface moderne, élégante et claire.
        </p>

        <div class="hero-actions">
            <a href="/admins/members-hub/" class="hero-btn hero-btn-light">← Retour espace membres</a>
            <a href="/admins/members/create/" class="hero-btn hero-btn-outline">➕ Créer un membre</a>
            <a href="/admins/members/export/" class="hero-btn hero-btn-outline">📥 Exporter Excel</a>
        </div>
    </div>

    <div class="section-card">
        <div class="section-head">
            <div>
                <h2>Recherche avancée</h2>
                <p>Retrouvez rapidement un membre à partir de son NIM ou de son numéro de téléphone.</p>
            </div>
        </div>

        <form method="GET" class="search-form">
            <div class="search-fields">
                <div class="field">
                    <label for="nim">Rechercher par NIM</label>
                    <input type="text" id="nim" name="nim" placeholder="Exemple : FAS-0000000012" value="{{ nim }}">
                </div>

                <div class="field">
                    <label for="phone">Rechercher par téléphone</label>
                    <input type="text" id="phone" name="phone" placeholder="Exemple : 0199999999" value="{{ phone }}">
                </div>
            </div>

            <div class="search-actions">
                <button type="submit" class="btn btn-primary">Rechercher</button>
                <a href="/admins/members/" class="btn btn-light">Réinitialiser</a>
            </div>
        </form>
    </div>

    <div class="table-box">
        <div class="table-top">
            <div>
                <h3>Membres enregistrés</h3>
                <p>Liste des membres avec accès rapide au détail de chaque profil.</p>
            </div>

            <div class="table-actions">
                <a href="/admins/members/create/" class="btn btn-primary">Créer un membre</a>
                <a href="/admins/members/export/" class="btn btn-success">Exporter Excel</a>
            </div>
        </div>

        <div class="table-wrap">
            <table>
                <tr>
                    <th>ID</th>
                    <th>NIM</th>
                    <th>Membre</th>
                    <th>Téléphone</th>
                    <th>Type de pièce</th>
                    <th>Statut</th>
                    <th>Action</th>
                </tr>

                {% for member in members %}
                <tr>
                    <td>{{ member.id }}</td>
                    <td class="nim">{{ member.nim }}</td>
                    <td>
                        <div class="member-name">{{ member.last_name }} {{ member.first_name }}</div>
                        <div class="member-sub">
                            {% if member.city %}
                                {{ member.city }}
                            {% else %}
                                Ville non renseignée
                            {% endif %}
                        </div>
                    </td>
                    <td>{{ member.phone|default:"-" }}</td>
                    <td>{{ member.id_card_type }}</td>
                    <td>
                        {% if member.status == 'active' %}
                            <span class="status status-active">Actif</span>
                        {% elif member.status == 'suspended' %}
                            <span class="status status-suspended">Suspendu</span>
                        {% else %}
                            <span class="status status-inactive">Inactif</span>
                        {% endif %}
                    </td>
                    <td>
                        <a href="/admins/members/{{ member.id }}/" class="btn-detail">Voir détail</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="7" class="empty">Aucun membre trouvé</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>

</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion membre</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #ffffff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #111827;
        }

        .container {
            width: 100%;
            max-width: 420px;
            background: white;
            padding: 35px 30px;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(15, 23, 42, 0.12);
            border: 1px solid #e5e7eb;
        }

        .header {
            text-align: center;
            margin-bottom: 25px;
        }

        .icon {
            width: 60px;
            height: 60px;
            margin: 0 auto 12px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .icon svg {
            width: 60px;
            height: 60px;
            display: block;
        }

        .header h1 {
            margin: 0;
            font-size: 28px;
            color: #111827;
        }

        .header p {
            margin-top: 8px;
            color: #6b7280;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 14px;
            border-radius: 12px;
            border: 1px solid #d1d5db;
            font-size: 15px;
            outline: none;
            transition: 0.3s;
            background: #fff;
        }

        input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.10);
        }

        .btn {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 12px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn:hover {
            background: #1d4ed8;
        }

        .hint {
            margin-top: 12px;
            font-size: 13px;
            color: #6b7280;
            text-align: center;
        }

        .footer {
            margin-top: 20px;
            text-align: center;
            font-size: 13px;
            color: #9ca3af;
        }

        @media (max-width: 500px) {
            .container {
                margin: 20px;
                padding: 28px 20px;
            }
        }
    </style>
</head>
<body>

    <div class="container">

        <div class="header">
            <div class="icon">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M10.49 2.23006L5.50003 4.10005C4.35003 4.53005 3.41003 5.89004 3.41003 7.12004V14.55C3.41003 15.73 4.19005 17.28 5.14005 17.99L9.44003 21.2001C10.85 22.2601 13.17 22.2601 14.58 21.2001L18.88 17.99C19.83 17.28 20.61 15.73 20.61 14.55V7.12004C20.61 5.89004 19.67 4.53005 18.52 4.10005L13.53 2.23006C12.68 1.92006 11.32 1.92006 10.49 2.23006Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    <path d="M12.0001 10.92C11.9601 10.92 11.9101 10.92 11.8701 10.92C10.9301 10.89 10.1801 10.11 10.1801 9.16003C10.1801 8.19003 10.9701 7.40002 11.9401 7.40002C12.9101 7.40002 13.7001 8.19003 13.7001 9.16003C13.6901 10.12 12.9401 10.89 12.0001 10.92Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    <path d="M10.01 13.72C9.05004 14.36 9.05004 15.41 10.01 16.05C11.1 16.78 12.89 16.78 13.98 16.05C14.94 15.41 14.94 14.36 13.98 13.72C12.9 12.99 11.11 12.99 10.01 13.72Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
            </div>
            <h1>Connexion membre</h1>
            <p>Accédez à votre espace personnel</p>
        </div>

        <form method="POST">
            {% csrf_token %}

            <div class="form-group">
                <label>NIM</label>
                <input type="text" name="nim" placeholder="Ex: FAS-0000000001" required>
            </div>

            <div class="form-group">
                <label>PIN (5 chiffres)</label>
                <input type="password" name="pin" maxlength="5" placeholder="•••••" required>
            </div>

            <button type="submit" class="btn">Se connecter</button>
        </form>

        <div class="hint">
            3 tentatives maximum avant blocage du compte
        </div>

        <div class="footer">
            Système sécurisé - FondAction
        </div>

    </div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil membre</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 78px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
            display: flex;
            align-items: center;
            margin-left: 0;
            margin-right: 0;
        }

        .header-logo img {
            height: 85px;
            width: auto;
            object-fit: contain;
            transform: translateX(-18px);
        }

        .header-nim {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            background: #f1f5f9;
            padding: 8px 12px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            line-height: 1.2;
        }

        .nim-label {
            font-size: 10px;
            color: #6b7280;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .nim-value {
            font-size: 13px;
            font-weight: bold;
            color: #111827;
        }

        .page {
            max-width: 500px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .title-box {
            margin-bottom: 18px;
        }

        .page-title {
            font-size: 28px;
            font-weight: bold;
            margin: 0 0 8px 0;
            color: #111827;
        }

        .page-subtitle {
            margin: 0;
            color: #6b7280;
            font-size: 14px;
            line-height: 1.6;
        }

        .profile-card {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            border-radius: 28px;
            padding: 22px 18px;
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
            margin-bottom: 18px;
        }

        .profile-top {
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 18px;
        }

        .profile-photo-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }

        .profile-photo {
            width: 86px;
            height: 86px;
            border-radius: 50%;
            overflow: hidden;
            border: 3px solid rgba(255,255,255,0.18);
            background: rgba(255,255,255,0.08);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .profile-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .profile-photo-empty {
            color: white;
            font-size: 12px;
            text-align: center;
            padding: 8px;
            line-height: 1.4;
        }

        .cert-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(59, 130, 246, 0.16);
            border: 1px solid rgba(96, 165, 250, 0.35);
            color: #bfdbfe;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: bold;
        }

        .cert-badge svg {
            width: 16px;
            height: 16px;
            fill: #3b82f6;
        }

        .profile-main {
            flex: 1;
            min-width: 0;
        }

        .profile-name {
            font-size: 24px;
            font-weight: bold;
            line-height: 1.25;
            margin-bottom: 8px;
            word-break: break-word;
        }

        .profile-status {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            background: rgba(255,255,255,0.1);
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #22c55e;
        }

        .status-suspended .status-dot {
            background: #ef4444;
        }

        .status-inactive .status-dot {
            background: #9ca3af;
        }

        .profile-meta-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }

        .meta-item {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 12px;
        }

        .meta-label {
            font-size: 12px;
            color: rgba(255,255,255,0.75);
            margin-bottom: 6px;
        }

        .meta-value {
            font-size: 14px;
            font-weight: bold;
            word-break: break-word;
        }

        .info-section {
            background: white;
            border-radius: 24px;
            padding: 20px 16px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        .section-title {
            margin: 0 0 16px 0;
            font-size: 22px;
            color: #111827;
        }

        .info-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .info-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 14px;
        }

        .info-icon {
            width: 42px;
            height: 42px;
            min-width: 42px;
            border-radius: 14px;
            background: #edf4ff;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .info-icon svg {
            width: 22px;
            height: 22px;
            stroke: #2563eb;
        }

        .info-content {
            flex: 1;
            min-width: 0;
        }

        .info-label {
            font-size: 13px;
            color: #6b7280;
            margin-bottom: 4px;
        }

        .info-value {
            font-size: 15px;
            font-weight: 600;
            color: #111827;
            line-height: 1.5;
            word-break: break-word;
            overflow-wrap: break-word;
        }

        .notice-box {
            background: #eef4ff;
            border: 1px solid #dbeafe;
            color: #1e3a8a;
            border-radius: 18px;
            padding: 16px 14px;
            font-size: 14px;
            line-height: 1.7;
            margin-top: 14px;
        }

        .footer-nav {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            border-top: 1px solid #e5e7eb;
            padding: 10px 8px 14px;
        }

        .footer-nav-inner {
            max-width: 500px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 4px;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 5px;
            color: #6b7280;
            padding: 8px 3px;
            border-radius: 14px;
            min-height: 62px;
            text-align: center;
            overflow: hidden;
        }

        .nav-item.active {
            background: #eaf2ff;
            color: #2563eb;
        }

        .nav-item svg {
            width: 22px;
            height: 22px;
            flex-shrink: 0;
        }

        .nav-label {
            font-size: 10px;
            font-weight: 600;
            line-height: 1.1;
            word-break: break-word;
            overflow-wrap: break-word;
            max-width: 100%;
        }

        @media (max-width: 420px) {
            .page-title {
                font-size: 24px;
            }

            .profile-top {
                align-items: flex-start;
            }

            .profile-name {
                font-size: 21px;
            }

            .profile-meta-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="header-logo">
            <img src="/static/images/logo.png" alt="FondAction Logo">
        </div>

        <div class="header-nim">
            <span class="nim-label">NIM</span>
            <span class="nim-value">{{ member.nim }}</span>
        </div>
    </header>

    <main class="page">
        <section class="title-box">
            <h1 class="page-title">Profil</h1>
            <p class="page-subtitle">
                Retrouvez ici vos informations personnelles.
            </p>
        </section>

        <section class="profile-card">
            <div class="profile-top">
                <div class="profile-photo-box">
                    <div class="profile-photo">
                        {% if member.photo %}
                            <img src="{{ member.photo.url }}" alt="Photo membre">
                        {% else %}
                            <div class="profile-photo-empty">Aucune photo</div>
                        {% endif %}
                    </div>

                    <div class="cert-badge">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M10.5857,2.10056 C11.3256895,1.36061789 12.5011493,1.32167357 13.2868927,1.98372704 L13.4141,2.10056 L15.3136,4.00005 L17.9999,4.00005 C19.0542909,4.00005 19.9180678,4.81592733 19.9944144,5.85078759 L19.9999,6.00005 L19.9999,8.68632 L21.8994,10.5858 C22.6393895,11.3257895 22.6783363,12.5012493 22.0162404,13.2870778 L21.8994,13.4143 L19.9999,15.3138 L19.9999,18.0001 C19.9999,19.0543955 19.18405,19.9182591 18.1491661,19.9946139 L17.9999,20.0001 L15.3136,20.0001 L13.4141,21.8995 C12.6742053,22.6394895 11.4987504,22.6784363 10.7129222,22.0163404 L10.5857,21.8995 L8.68622,20.0001 L5.99991,20.0001 C4.94554773,20.0001 4.08174483,19.1841589 4.00539573,18.1493537 L3.99991,18.0001 L3.99991,15.3137 L2.10043,13.4143 C1.36049737,12.6743105 1.32155355,11.4988507 1.98360703,10.7130222 L2.10044,10.5858 L3.99991,8.68636 L3.99991,6.00005 C3.99991,4.94568773 4.81578733,4.08188483 5.85064759,4.00553573 L5.99991,4.00005 L8.68622,4.00005 L10.5857,2.10056 Z M11.9999,3.51477 L10.1004,5.41426 C9.76703111,5.74766444 9.32804642,5.9511963 8.86207199,5.99230949 L8.68622,6.00005 L5.99991,6.00005 L5.99991,8.68636 C5.99991,9.15786222 5.83342309,9.61218716 5.53299532,9.97077196 L5.41412,10.1006 L3.51465,12.0001 L5.41412,13.8995 C5.74752444,14.2329222 5.9510563,14.6719049 5.99216949,15.1378572 L5.99991,15.3137 L5.99991,18.0001 L8.68622,18.0001 C9.15772222,18.0001 9.61204716,18.166579 9.97058982,18.4669488 L10.1004,18.5858 L11.9999,20.4853 L13.8994,18.5858 C14.2328222,18.2524667 14.6718049,18.0489506 15.1377572,18.0078401 L15.3136,18.0001 L17.9999,18.0001 L17.9999,15.3138 C17.9999,14.8422444 18.166379,14.3879136 18.4668191,14.0293984 L18.5857,13.8996 L20.4852,12.0001 L18.5857,10.1005 C18.2522778,9.76714 18.0487519,9.3281563 18.0076402,8.86217495 L17.9999,8.68632 L17.9999,6.00005 L15.3136,6.00005 C14.8421333,6.00005 14.3878123,5.83356309 14.029228,5.53313532 L13.8994,5.41426 L11.9999,3.51477 Z M15.0793,8.98261 C15.4698,8.59209 16.103,8.59209 16.4935,8.98261 C16.8540538,9.34309923 16.8817888,9.91032645 16.5767047,10.3025979 L16.4935,10.3968 L11.6126,15.2778 C11.2136857,15.6766214 10.5846383,15.7051087 10.1529279,15.3632617 L10.057,15.2778 L7.6528,12.8736 C7.26228,12.4831 7.26228,11.8499 7.6528,11.4594 C8.01328,11.0989385 8.58051503,11.0712107 8.9728035,11.3762166 L9.06701,11.4594 L10.8348,13.2271 L15.0793,8.98261 Z"></path>
                        </svg>
                        <span>Compte certifié</span>
                    </div>
                </div>

                <div class="profile-main">
                    <div class="profile-name">
                        {{ member.last_name|default:"" }} {{ member.first_name|default:"" }}
                    </div>

                    {% if member.status == 'active' %}
                        <div class="profile-status">
                            <span class="status-dot"></span>
                            <span>Membre actif</span>
                        </div>
                    {% elif member.status == 'suspended' %}
                        <div class="profile-status status-suspended">
                            <span class="status-dot"></span>
                            <span>Membre suspendu</span>
                        </div>
                    {% else %}
                        <div class="profile-status status-inactive">
                            <span class="status-dot"></span>
                            <span>Membre inactif</span>
                        </div>
                    {% endif %}
                </div>
            </div>

            <div class="profile-meta-grid">
                <div class="meta-item">
                    <div class="meta-label">NIM</div>
                    <div class="meta-value">{{ member.nim|default:"—" }}</div>
                </div>

            </div>
        </section>

        <section class="info-section">
            <h2 class="section-title">Informations personnelles</h2>

            <div class="info-list">
                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Nom complet</div>
                        <div class="info-value">{{ member.last_name|default:"—" }} {{ member.first_name|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Téléphone</div>
                        <div class="info-value">{{ member.phone|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Date de naissance</div>
                        <div class="info-value">{{ member.birth_date|date:"d/m/Y"|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Lieu de naissance</div>
                        <div class="info-value">{{ member.birth_place|default:"—" }}</div>
                    </div>
                </div>


<div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205 3 1m1.5.5-1.5-.5M6.75 7.364V3h-3v18m3-13.636 10.5-3.819" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Département</div>
                        <div class="info-value">{{ member.department|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205 3 1m1.5.5-1.5-.5M6.75 7.364V3h-3v18m3-13.636 10.5-3.819" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Commune</div>
                        <div class="info-value">{{ member.commune|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205 3 1m1.5.5-1.5-.5M6.75 7.364V3h-3v18m3-13.636 10.5-3.819" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Ville</div>
                        <div class="info-value">{{ member.city|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Quartier / Arrondissement</div>
                        <div class="info-value">{{ member.district|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Type de pièce</div>
                        <div class="info-value">{{ member.id_card_type|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Numéro de pièce</div>
                        <div class="info-value">{{ member.id_card_number|default:"—" }}</div>
                    </div>
                </div>

                <div class="info-item">
                    <div class="info-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5" />
                        </svg>
                    </div>
                    <div class="info-content">
                        <div class="info-label">Date d’adhésion</div>
                        <div class="info-value">{{ member.created_at|date:"d/m/Y"|default:"—" }}</div>
                    </div>
                </div>
            </div>

            <div class="notice-box">
                En cas d’anomalie ou de non-conformité dans vos informations, merci de contacter l’administration pour correction.
            </div>
        </section>
    </main>

    <nav class="footer-nav">
        <div class="footer-nav-inner">
            <a href="/admins/member-space/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>
                <div class="nav-label">Accueil</div>
            </a>

            <a href="/admins/member-card/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                </svg>
                <div class="nav-label">Carte</div>
            </a>

            <a href="/admins/member-infos/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
                </svg>
                <div class="nav-label">Infos</div>
            </a>

            <a href="/admins/member-profile/" class="nav-item active">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Profil</div>
            </a>

            <a href="/admins/member-settings/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Paramètres</div>
            </a>
        </div>
    </nav>

</body>
</html>                





{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paramètres</title>

    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 78px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
            display: flex;
            align-items: center;
            margin-left: 0px;
            margin-right: 0px;
        }

        .header-logo img {
            height: 85px;
            width: auto;
            object-fit: contain;
            transform: translateX(-18px);
        }

        .header-nim {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            background: #f1f5f9;
            padding: 8px 12px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            line-height: 1.2;
        }

        .nim-label {
            font-size: 10px;
            color: #6b7280;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .nim-value {
            font-size: 13px;
            font-weight: bold;
            color: #111827;
        }

        .page {
            max-width: 500px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .title-box {
            margin-bottom: 18px;
        }

        .page-title {
            font-size: 28px;
            font-weight: bold;
            margin: 0 0 8px 0;
            color: #111827;
        }

        .page-subtitle {
            margin: 0;
            color: #6b7280;
            font-size: 14px;
            line-height: 1.7;
        }

        .settings-card {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            border-radius: 28px;
            padding: 22px 18px;
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
            margin-bottom: 18px;
        }

        .settings-card-title {
            font-size: 22px;
            font-weight: bold;
            margin: 0 0 10px 0;
        }

        .settings-card-text {
            margin: 0;
            font-size: 14px;
            line-height: 1.8;
            color: rgba(255,255,255,0.86);
        }

        .settings-section {
            background: white;
            border-radius: 24px;
            padding: 18px 16px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        .section-title {
            margin: 0 0 16px 0;
            font-size: 22px;
            color: #111827;
        }

        .settings-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .setting-item {
            display: flex;
            align-items: center;
            gap: 12px;
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 14px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .setting-item:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 18px rgba(15, 23, 42, 0.06);
        }

        .setting-icon {
            width: 48px;
            height: 48px;
            min-width: 48px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #edf4ff;
        }

        .setting-icon svg {
            width: 24px;
            height: 24px;
        }

        .setting-content {
            flex: 1;
            min-width: 0;
        }

        .setting-title {
            font-size: 15px;
            font-weight: bold;
            color: #111827;
            margin-bottom: 4px;
        }

        .setting-text {
            font-size: 13px;
            color: #6b7280;
            line-height: 1.5;
            word-break: break-word;
            overflow-wrap: break-word;
        }

        .setting-arrow {
            color: #94a3b8;
            font-size: 20px;
            font-weight: bold;
            line-height: 1;
        }

        .password-item .setting-icon {
            background: #eef4ff;
        }

        .password-item .setting-icon svg path {
            stroke: #2563eb;
        }

        .help-item .setting-icon {
            background: #f0fdf4;
        }

        .help-item .setting-icon svg {
            fill: #16a34a;
        }

        .logout-item .setting-icon {
            background: #fef2f2;
        }

        .logout-item .setting-icon svg path {
            fill: #dc2626;
        }

        .notice-box {
            background: #fff7ed;
            border: 1px solid #fed7aa;
            color: #9a3412;
            border-radius: 18px;
            padding: 15px 14px;
            font-size: 14px;
            line-height: 1.7;
            margin-top: 14px;
        }

        .footer-nav {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(12px);
            border-top: 1px solid #e5e7eb;
            padding: 10px 8px 14px;
        }

        .footer-nav-inner {
            max-width: 500px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 4px;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 5px;
            color: #6b7280;
            padding: 8px 3px;
            border-radius: 14px;
            min-height: 62px;
            text-align: center;
            overflow: hidden;
        }

        .nav-item.active {
            background: #eaf2ff;
            color: #2563eb;
        }

        .nav-item svg {
            width: 22px;
            height: 22px;
            flex-shrink: 0;
        }

        .nav-label {
            font-size: 10px;
            font-weight: 600;
            line-height: 1.1;
            word-break: break-word;
            overflow-wrap: break-word;
            max-width: 100%;
        }

        @media (max-width: 420px) {
            .page-title {
                font-size: 24px;
            }

            .settings-card-title {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="header-logo">
            <img src="/static/images/logo.png" alt="FondAction Logo">
        </div>

        <div class="header-nim">
            <span class="nim-label">NIM</span>
            <span class="nim-value">{{ member.nim }}</span>
        </div>
    </header>

    <main class="page">
        <section class="title-box">
            <h1 class="page-title">Paramètres</h1>
            
        </section>

        <section class="settings-card">
            <h2 class="settings-card-title">Sécurité et assistance</h2>
            <p class="settings-card-text">
                Utilisez ces options pour protéger votre compte, obtenir de l’aide si nécessaire
                et gérer votre session en toute simplicité.
            </p>
        </section>

        <section class="settings-section">
            <h2 class="section-title">Options</h2>

            <div class="settings-list">
                <a href="/admins/member-change-pin/" class="setting-item password-item">
                    <div class="setting-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20.91 11.12C20.91 16.01 17.36 20.59 12.51 21.93C12.18 22.02 11.82 22.02 11.49 21.93C6.63996 20.59 3.08997 16.01 3.08997 11.12V6.72997C3.08997 5.90997 3.70998 4.97998 4.47998 4.66998L10.05 2.39001C11.3 1.88001 12.71 1.88001 13.96 2.39001L19.53 4.66998C20.29 4.97998 20.92 5.90997 20.92 6.72997L20.91 11.12Z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                            <path d="M12 12.5C13.1046 12.5 14 11.6046 14 10.5C14 9.39543 13.1046 8.5 12 8.5C10.8954 8.5 10 9.39543 10 10.5C10 11.6046 10.8954 12.5 12 12.5Z" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"></path>
                            <path d="M12 12.5V15.5" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"></path>
                        </svg>
                    </div>
                    <div class="setting-content">
                        <div class="setting-title">Changer mon mot de passe</div>
                        <div class="setting-text">Modifiez votre code d’accès personnel pour renforcer la sécurité de votre compte.</div>
                    </div>
                    <div class="setting-arrow">›</div>
                </a>

                <a href="/admins/member-assistance/" class="setting-item help-item">
                    <div class="setting-icon">
                        <svg fill="#16a34a" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 33.834 33.834" xml:space="preserve">
                            <g>
                                <path d="M32.253,29.334v4.5H1.581v-4.501c0-2.125,1.832-4.741,4.07-5.804l4.98-2.366l3.457,7.204l1.77-4.799 c0.349,0.066,0.695,0.154,1.059,0.154s0.709-0.088,1.059-0.154l1.68,4.563l3.389-7.048l5.141,2.445 C30.421,24.591,32.253,27.207,32.253,29.334z M6.105,13.562v-3.25c0-0.551,0.287-1.034,0.72-1.312c0.581-5.058,4.883-9,10.094-9 s9.514,3.942,10.096,9c0.432,0.278,0.719,0.761,0.719,1.312v3.25c0,0.863-0.699,1.563-1.563,1.563s-1.563-0.7-1.563-1.563v-0.683 c-0.846,4.255-3.961,8.205-7.688,8.205c-3.727,0-6.842-3.95-7.688-8.205v0.683c0,0.7-0.465,1.286-1.1,1.485 c0.622,2.117,2.002,3.946,3.908,5.146c0.352-0.116,0.796-0.094,1.227,0.13c0.692,0.36,1.045,1.06,0.783,1.56 c-0.261,0.5-1.033,0.612-1.729,0.251c-0.508-0.265-0.83-0.71-0.864-1.126c-2.183-1.396-3.731-3.533-4.37-5.998 C6.513,14.78,6.105,14.22,6.105,13.562z M7.89,8.635c0.047,0.003,0.092,0.004,0.137,0.021C8.14,8.698,8.222,8.779,8.279,8.874 c0.339,0.144,0.609,0.407,0.775,0.733C9.515,5.286,12.855,3,16.917,3c4.062,0,7.402,2.286,7.863,6.607 c0.229-0.449,0.664-0.77,1.185-0.837c-0.676-4.393-4.47-7.771-9.048-7.771C12.386,1,8.622,4.309,7.89,8.635z"></path>
                            </g>
                        </svg>
                    </div>
                    <div class="setting-content">
                        <div class="setting-title">Assistance</div>
                        <div class="setting-text">Besoin d’aide ou d’un accompagnement ? Contactez l’administration pour toute assistance.</div>
                    </div>
                    <div class="setting-arrow">›</div>
                </a>


<a href="/admins/member-logout/" class="setting-item logout-item">
                    <div class="setting-icon">
                        <svg viewBox="0 -0.5 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M11.75 9.874C11.75 10.2882 12.0858 10.624 12.5 10.624C12.9142 10.624 13.25 10.2882 13.25 9.874H11.75ZM13.25 4C13.25 3.58579 12.9142 3.25 12.5 3.25C12.0858 3.25 11.75 3.58579 11.75 4H13.25ZM9.81082 6.66156C10.1878 6.48991 10.3542 6.04515 10.1826 5.66818C10.0109 5.29121 9.56615 5.12478 9.18918 5.29644L9.81082 6.66156ZM5.5 12.16L4.7499 12.1561L4.75005 12.1687L5.5 12.16ZM12.5 19L12.5086 18.25C12.5029 18.25 12.4971 18.25 12.4914 18.25L12.5 19ZM19.5 12.16L20.2501 12.1687L20.25 12.1561L19.5 12.16ZM15.8108 5.29644C15.4338 5.12478 14.9891 5.29121 14.8174 5.66818C14.6458 6.04515 14.8122 6.48991 15.1892 6.66156L15.8108 5.29644ZM13.25 9.874V4H11.75V9.874H13.25ZM9.18918 5.29644C6.49843 6.52171 4.7655 9.19951 4.75001 12.1561L6.24999 12.1639C6.26242 9.79237 7.65246 7.6444 9.81082 6.66156L9.18918 5.29644ZM4.75005 12.1687C4.79935 16.4046 8.27278 19.7986 12.5086 19.75L12.4914 18.25C9.08384 18.2892 6.28961 15.5588 6.24995 12.1513L4.75005 12.1687ZM12.4914 19.75C16.7272 19.7986 20.2007 16.4046 20.2499 12.1687L18.7501 12.1513C18.7104 15.5588 15.9162 18.2892 12.5086 18.25L12.4914 19.75ZM20.25 12.1561C20.2345 9.19951 18.5016 6.52171 15.8108 5.29644L15.1892 6.66156C17.3475 7.6444 18.7376 9.79237 18.75 12.1639L20.25 12.1561Z" fill="#dc2626"></path>
                        </svg>
                    </div>
                    <div class="setting-content">
                        <div class="setting-title">Déconnexion</div>
                        <div class="setting-text">Fermez votre session actuelle en toute sécurité.</div>
                    </div>
                    <div class="setting-arrow">›</div>
                </a>
            </div>

            <div class="notice-box">
                Pour toute difficulté d’accès, de sécurité ou d’assistance, rapprochez-vous de l’administration afin d’obtenir un accompagnement adapté.
            </div>
        </section>
    </main>

    <nav class="footer-nav">
        <div class="footer-nav-inner">
            <a href="/admins/member-space/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>
                <div class="nav-label">Accueil</div>
            </a>

            <a href="/admins/member-card/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                </svg>
                <div class="nav-label">Carte</div>
            </a>

            <a href="/admins/member-infos/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
                </svg>
                <div class="nav-label">Infos</div>
            </a>

            <a href="/admins/member-profile/" class="nav-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Profil</div>
            </a>

            <a href="/admins/member-settings/" class="nav-item active">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
                <div class="nav-label">Paramètres</div>
            </a>
        </div>
    </nav>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Espace membre</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 78px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
    display: flex;
    align-items: center;

    /* 👉 contrôle position horizontale */
    margin-left: 0px;   /* déplace à droite */
    margin-right: 0px;  /* déplace à gauche */
}

.header-logo img {
    /* 👉 contrôle taille */
    height: 85px;   /* change ici */
    width: auto;

    object-fit: contain;

    /* 👉 contrôle position fine */
    transform: translateX(-18px); /* décalage gauche/droite */
}

        .header-nim {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    background: #f1f5f9;
    padding: 8px 12px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    line-height: 1.2;
}

.nim-label {
    font-size: 10px;
    color: #6b7280;
    font-weight: 600;
    letter-spacing: 1px;
}

.nim-value {
    font-size: 13px;
    font-weight: bold;
    color: #111827;
}

        .page {
            max-width: 500px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .welcome-box {
            margin-top: 6px;
            margin-bottom: 18px;
        }

        .welcome-label {
            font-size: 15px;
            color: #6b7280;
            margin-bottom: 6px;
        }

        .welcome-name {
            font-size: 15px;
            color: #6b7280;
            margin-bottom: 4px;
        }

        .welcome-fullname {
            font-size: 28px;
            font-weight: bold;
            color: #111827;
            line-height: 1.25;
            word-break: break-word;
        }

        .balance-card {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            border-radius: 28px;
            padding: 24px 20px;
            color: white;
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
            margin-bottom: 24px;
        }

        .balance-label {
            font-size: 14px;
            color: rgba(255,255,255,0.78);
            margin-bottom: 10px;
        }

        .balance-value {
            font-size: 34px;
            font-weight: bold;
            line-height: 1.15;
            word-break: break-word;
            margin-bottom: 16px;
        }

        .balance-bottom {
            border-top: 1px solid rgba(255,255,255,0.12);
            padding-top: 14px;
        }

        .balance-text {
            margin: 0;
            font-size: 14px;
            color: rgba(255,255,255,0.88);
            line-height: 1.8;
        }

        .actions-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
        }

        .action-item {
            background: white;
            border-radius: 24px;
            padding: 18px 10px 16px;
            text-align: center;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.07);
            border: 1px solid #edf2f7;
            min-height: 126px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 14px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .action-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 30px rgba(15, 23, 42, 0.1);
        }

        .action-icon {
            width: 62px;
            height: 62px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8fafc;
            box-shadow: inset 0 0 0 1px #e5e7eb;
        }

        .action-item:nth-child(1) .action-icon {
            background: #eaf2ff;
        }

        .action-item:nth-child(2) .action-icon {
            background: #ecfdf3;
        }

        .action-item:nth-child(3) .action-icon {
            background: #ecfeff;
        }

        .action-icon svg {
            width: 34px;
            height: 34px;
        }

        .action-title {
            font-size: 15px;
            font-weight: bold;
            color: #111827;
            line-height: 1.3;
        }

        .footer-nav {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(12px);
    border-top: 1px solid #e5e7eb;
    padding: 10px 8px 14px;
}

.footer-nav-inner {
    max-width: 500px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 4px;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 5px;
    color: #6b7280;
    padding: 8px 3px;
    border-radius: 14px;
    min-height: 62px;
    text-align: center;
    overflow: hidden;
}

.nav-item.active {
    background: #eaf2ff;
    color: #2563eb;
}

.nav-item svg {
    width: 22px;
    height: 22px;
    flex-shrink: 0;
}

.nav-label {
    font-size: 10px;
    font-weight: 600;
    line-height: 1.1;
    word-break: break-word;
    overflow-wrap: break-word;
    max-width: 100%;
}

        @media (max-width: 420px) {
            .header-title {
                font-size: 20px;
            }

            .welcome-fullname {
                font-size: 24px;
            }

            .balance-value {
                font-size: 30px;
            }

            .action-item {
                min-height: 118px;
                padding: 16px 8px 14px;
            }

            .action-icon {
                width: 56px;
                height: 56px;
            }

            .action-title {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>

    <header class="header">
    <div class="header-logo">
    <img src="/static/images/logo.png" alt="FondAction Logo">
</div>

    <div class="header-nim">
        <span class="nim-label">NIM</span>
        <span class="nim-value">{{ member.nim }}</span>
    </div>
</header>

    <main class="page">
        <section class="welcome-box">
            <div class="welcome-label">Bienvenue</div>
            
            <div class="welcome-fullname">
                {{ member.last_name|default:"" }} {{ member.first_name|default:"" }}
            </div>
        </section>

        <section class="balance-card">
            <div class="balance-label">Montant total cotisé</div>
            <div class="balance-value">{{ total_contributions|default:"0.00" }} FCFA</div>

            <div class="balance-bottom">
                <p class="balance-text">
                    Votre contribution participe à bâtir notre avenir commun.
                    Merci de faire partie de cette communauté engagée.
                </p>
            </div>
        </section>

        <section class="actions-grid">
            <a href="/admins/member-payment/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="-0.5 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 10.9199V2.91992" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M14.8008 6.11992L18.0008 2.91992L21.2008 6.11992" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M10.58 3.96997H6C4.93913 3.96997 3.92178 4.39146 3.17163 5.1416C2.42149 5.89175 2 6.9091 2 7.96997V17.97C2 19.0308 2.42149 20.0482 3.17163 20.7983C3.92178 21.5485 4.93913 21.97 6 21.97H18C19.0609 21.97 20.0783 21.5485 20.8284 20.7983C21.5786 20.0482 22 19.0308 22 17.97V13.8999" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M2 9.96997H5.37006C6.16571 9.96997 6.92872 10.286 7.49133 10.8486C8.05394 11.4112 8.37006 12.1743 8.37006 12.97C8.37006 13.7656 8.05394 14.5287 7.49133 15.0913C6.92872 15.6539 6.16571 15.97 5.37006 15.97H2" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </div>
                <div class="action-title">Payer</div>
            </a>

            <a href="/admins/member-withdrawal/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" fill="#16a34a">
                        <path fill="#16a34a" d="M258 21.89c-.5 0-1.2 0-1.8.12-4.6.85-10.1 5.1-13.7 14.81-3.8 9.7-4.6 23.53-1.3 38.34 3.4 14.63 10.4 27.24 18.2 34.94 7.6 7.7 14.5 9.8 19.1 9 4.8-.7 10.1-5.1 13.7-14.7 3.8-9.64 4.8-23.66 1.4-38.35-3.5-14.8-10.4-27.29-18.2-34.94-6.6-6.8-12.7-9.22-17.4-9.22zM373.4 151.4c-11 .3-24.9 3.2-38.4 8.9-15.6 6.8-27.6 15.9-34.2 24.5-6.6 8.3-7.2 14.6-5.1 18.3 2.2 3.7 8.3 7.2 20 7.7 11.7.7 27.5-2.2 43-8.8 15.5-6.7 27.7-15.9 34.3-24.3 6.6-8.3 7.1-14.8 5-18.5-2.1-3.8-8.3-7.1-20-7.5-1.6-.3-3-.3-4.6-.3zm-136.3 92.9c-6.6.1-12.6.9-18 2.3-11.8 3-18.6 8.4-20.8 14.9-2.5 6.5 0 14.3 7.8 22.7 8.2 8.2 21.7 16.1 38.5 20.5 16.7 4.4 32.8 4.3 44.8 1.1 12.1-3.1 18.9-8.6 21.1-15 2.3-6.5 0-14.2-8.1-22.7-7.9-8.2-21.4-16.1-38.2-20.4-9.5-2.5-18.8-3.5-27.1-3.4zm160.7 58.1L336 331.7c4.2.2 14.7.5 14.7.5l6.6 8.7 54.7-28.5-14.2-10zm-54.5.1l-57.4 27.2c5.5.3 18.5.5 23.7.8l49.8-23.6-16.1-4.4zm92.6 10.8l-70.5 37.4 14.5 18.7 74.5-44.6-18.5-11.5zm-278.8 9.1a40.33 40.33 0 0 0-9 1c-71.5 16.5-113.7 17.9-126.2 17.9H18v107.5s11.6-1.7 30.9-1.8c37.3 0 103 6.4 167 43.8 3.4 2.1 10.7 2.9 19.8 2.9 24.3 0 61.2-5.8 69.7-9C391 452.6 494 364.5 494 364.5l-32.5-28.4s-79.8 50.9-89.9 55.8c-91.1 44.7-164.9 16.8-164.9 16.8s119.9 3 158.4-27.3l-22.6-34s-82.8-2.3-112.3-6.2c-15.4-2-48.7-18.8-73.1-18.8z"></path>
                    </svg>
                </div>
                <div class="action-title">Retrait</div>
            </a>

            <a href="/admins/member-transactions/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" fill="#0f766e">
                        <path d="M52,7H12a6,6,0,0,0-6,6V51a6,6,0,0,0,6,6H52a6,6,0,0,0,6-6V13A6,6,0,0,0,52,7Zm2,44a2,2,0,0,1-2,2H12a2,2,0,0,1-2-2V13a2,2,0,0,1,2-2H52a2,2,0,0,1,2,2Z"></path>
                        <path d="M45,29a2,2,0,0,0,0-4H22.83l2.58-2.59a2,2,0,0,0-2.82-2.82l-6,6a2,2,0,0,0-.44,2.18A2,2,0,0,0,18,29Z"></path>
                        <path d="M47,36H20a2,2,0,0,0,0,4H42.17l-2.58,2.59a2,2,0,1,0,2.82,2.82l6-6a2,2,0,0,0,.44-2.18A2,2,0,0,0,47,36Z"></path>
                    </svg>
                </div>
                <div class="action-title">Transactions</div>
            </a>
        </section>
    </main>

<nav class="footer-nav">
    <div class="footer-nav-inner">
        <a href="/admins/member-space/" class="nav-item active">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
            </svg>
            <div class="nav-label">Accueil</div>
        </a>

        <a href="/admins/member-card/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
            </svg>
            <div class="nav-label">Carte</div>
        </a>

        <a href="/admins/member-infos/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
            </svg>
            <div class="nav-label">Infos</div>
        </a>

        <a href="/admins/member-profile/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Profil</div>
        </a>

        <a href="/admins/member-settings/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Paramètres</div>
        </a>
    </div>
</nav>

</body>
</html>



{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reçu de transaction</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-bottom: 40px;
        }

        .page {
            max-width: 620px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .simple-header {
            background: white;
            border-radius: 24px;
            padding: 22px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        .simple-header h1 {
            margin: 0;
            font-size: 28px;
            font-weight: bold;
            color: #111827;
        }

        .header-actions {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 12px;
        }

        .back-btn,
        .download-btn {
            display: inline-block;
            background: #111827;
            color: white;
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            transition: 0.2s ease;
            border: none;
            cursor: pointer;
        }

        .download-btn {
            background: #16a34a;
        }

        .back-btn:hover {
            background: #000;
            transform: translateY(-1px);
        }

        .download-btn:hover {
            background: #15803d;
            transform: translateY(-1px);
        }

        .receipt-wrapper {
            background: white;
            border-radius: 24px;
            padding: 22px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
        }

        .receipt {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 22px;
            overflow: hidden;
        }

        .receipt-top {
    background: #ffffff;   /* fond blanc */
    color: #111827;        /* texte noir */
    border-bottom: 1px solid #e5e7eb;
}

        .receipt-brand {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }

        .receipt-logo-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .receipt-logo {
            height: 54px;
            width: auto;
            object-fit: contain;
        }

        .receipt-brand-text h2 {
            margin: 0;
            font-size: 22px;
            line-height: 1.2;
        }

        .receipt-brand-text p {
    color: #6b7280; /* gris normal au lieu de blanc */
}

        .receipt-status {
            text-align: right;
        }

        .receipt-status-label {
    color: #6b7280;
}

        .status-badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .success {
            background: #dcfce7;
            color: #166534;
        }

        .pending {
            background: #fef3c7;
            color: #92400e;
        }

        .failed {
            background: #fee2e2;
            color: #991b1b;
        }

        .receipt-body {
            padding: 18px;
        }

        .receipt-title-box {
            margin-bottom: 18px;
        }

        .receipt-title {
            margin: 0;
            font-size: 24px;
            color: #111827;
        }

        .receipt-subtitle {
            margin: 8px 0 0 0;
            color: #6b7280;
            font-size: 14px;
            line-height: 1.6;
        }

        .amount-box {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 16px;
            text-align: center;
        }

        .amount-label {
            font-size: 13px;
            color: #6b7280;
            margin-bottom: 8px;
        }

        .amount-value {
            font-size: 30px;
            font-weight: bold;
            color: #166534;
            line-height: 1.2;
        }

        .detail-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 16px;
        }

        .detail-item {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 14px;
        }

        .detail-item.full {
            grid-column: 1 / -1;
        }

        .detail-label {
            font-size: 13px;
            color: #6b7280;
            margin-bottom: 5px;
        }

        .detail-value {
            font-size: 15px;
            font-weight: 600;
            color: #111827;
            line-height: 1.6;
            word-break: break-word;
            overflow-wrap: break-word;
        }

        .section-box {
            margin-top: 10px;
            margin-bottom: 16px;
        }

        .section-box h3 {
            margin: 0 0 12px 0;
            font-size: 18px;
            color: #111827;
        }

        .receipt-note {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1e3a8a;
            border-radius: 14px;
            padding: 14px 16px;
            line-height: 1.7;
            font-size: 14px;
        }

        .receipt-footer {
            border-top: 1px dashed #d1d5db;
            padding: 16px 18px 20px;
            text-align: center;
            color: #6b7280;
            font-size: 13px;
            line-height: 1.7;
        }

        .receipt-footer strong {
            color: #111827;
        }

        @media (max-width: 640px) {
            .simple-header h1 {
                font-size: 24px;
            }

            .receipt-brand {
                flex-direction: column;
                align-items: flex-start;
            }

            .receipt-status {
                text-align: left;
            }

            .receipt-brand-text h2 {
                font-size: 20px;
            }

            .amount-value {
                font-size: 26px;
            }

            .detail-grid {
                grid-template-columns: 1fr;
            }
        }

        @media print {
            body {
                background: white;
            }

            .simple-header {
                display: none;
            }

            .receipt-wrapper {
                box-shadow: none;
                padding: 0;
                background: transparent;
            }

            .receipt {
                border: none;
                box-shadow: none;
            }
        }

        .receipt-header-centered {
    text-align: center;
    padding: 18px 10px;
}

.receipt-main-title {
    margin: 0;
    font-size: 22px;
    font-weight: bold;
    color: #111827;
}

.receipt-sub-title {
    margin: 6px 0 10px 0;
    font-size: 14px;
    color: #6b7280;
}

.receipt-status-centered {
    margin-top: 6px;
}

    </style>
</head>
<body>

<div class="page">
    <div class="simple-header">
        <h1>Reçu de transaction</h1>
        <div class="header-actions">
            <a href="/admins/member-transactions/" class="back-btn">Retour aux transactions</a>
            <button type="button" class="download-btn" onclick="downloadReceiptPDF()">Télécharger le reçu</button>
        </div>
    </div>

    <div class="receipt-wrapper" id="receipt-area">
        <div class="receipt">
            <div class="receipt-top">
                <div class="receipt-header-centered">
    <h2 class="receipt-main-title">FondAction SARL</h2>
    <p class="receipt-sub-title">Reçu officiel de transaction</p>

    <div class="receipt-status-centered">
        {% if transaction.status == 'success' %}
            <span class="status-badge success">Succès</span>
        {% elif transaction.status == 'pending' %}
            <span class="status-badge pending">En attente</span>
        {% else %}
            <span class="status-badge failed">Échoué</span>
        {% endif %}
    </div>
</div>
            </div>

            <div class="receipt-body">
                <div class="receipt-title-box">
                    <h2 class="receipt-title">Reçu n° {{ transaction.reference }}</h2>
                    <p class="receipt-subtitle">
                        Ce document atteste l’enregistrement de votre opération dans le système FondAction.
                    </p>
                </div>

                <div class="amount-box">
                    <div class="amount-label">Montant de l’opération</div>
                    <div class="amount-value">{{ transaction.amount }} FCFA</div>
                </div>

                <div class="detail-grid">
                    <div class="detail-item">
                        <div class="detail-label">Référence</div>
                        <div class="detail-value">{{ transaction.reference }}</div>
                    </div>

                    <div class="detail-item">
                      <div class="detail-label">Numéro de reçu</div>
                      <div class="detail-value">{{ transaction.receipt_number|default:"—" }}</div>
                    </div>

                    <div class="detail-item">
                        <div class="detail-label">Type de transaction</div>
                        <div class="detail-value">{{ transaction.transaction_type }}</div>
                    </div>

                    <div class="detail-item">
                        <div class="detail-label">Nom du membre</div>
                        <div class="detail-value">{{ member.last_name }} {{ member.first_name }}</div>
                    </div>

                    <div class="detail-item">
                        <div class="detail-label">NIM</div>
                        <div class="detail-value">{{ member.nim }}</div>
                    </div>

                    <div class="detail-item">
                        <div class="detail-label">Date de création</div>
                        <div class="detail-value">{{ transaction.created_at|date:"d/m/Y H:i" }}</div>
                    </div>

                    <div class="detail-item">
                        <div class="detail-label">Date de validation</div>
                        <div class="detail-value">
                            {% if transaction.validated_at %}
                                {{ transaction.validated_at|date:"d/m/Y H:i" }}
                            {% else %}
                                —
                            {% endif %}
                        </div>
                    </div>

                    <div class="detail-item full">
                        <div class="detail-label">Description</div>
                        <div class="detail-value">{{ transaction.description|default:"—" }}</div>
                    </div>
                </div>

                {% if withdrawal_request %}
                <div class="section-box">
                    <h3>Détails du retrait</h3>

                    <div class="detail-grid">
                        <div class="detail-item">
                            <div class="detail-label">Numéro destinataire</div>
                            <div class="detail-value">{{ withdrawal_request.receiver_phone }}</div>
                        </div>

                        <div class="detail-item">
                            <div class="detail-label">Statut de la demande</div>
                            <div class="detail-value">{{ withdrawal_request.status }}</div>
                        </div>

                        <div class="detail-item full">
                            <div class="detail-label">Motif</div>
                            <div class="detail-value">{{ withdrawal_request.reason|default:"—" }}</div>
                        </div>

                        <div class="detail-item">
                            <div class="detail-label">Traité le</div>
                            <div class="detail-value">
                                {% if withdrawal_request.processed_at %}
                                    {{ withdrawal_request.processed_at|date:"d/m/Y H:i" }}
                                {% else %}
                                    —
                                {% endif %}
                            </div>
                        </div>

                        <div class="detail-item">
                            <div class="detail-label">Note admin</div>
                            <div class="detail-value">{{ withdrawal_request.admin_note|default:"—" }}</div>
                        </div>
                    </div>
                </div>
                {% endif %}

                <div class="receipt-note">
                    Conservez ce reçu comme justificatif. Il peut être téléchargé en PDF et présenté en cas de besoin.
                </div>
            </div>

            <div class="receipt-footer">
                <div><strong>FondAction SARL</strong></div>
                <div>Document généré depuis l’espace membre</div>
                <div>Date d’émission : {% now "d/m/Y H:i" %}</div>
            </div>
        </div>
    </div>
</div>

<script src="{% static 'js/html2canvas.min.js' %}"></script>
<script src="{% static 'js/jspdf.umd.min.js' %}"></script>

<script>
async function waitForImages(container) {
    const images = container.querySelectorAll('img');
    const promises = [];

    images.forEach((img) => {
        if (img.complete) {
            return;
        }

        promises.push(new Promise((resolve) => {
            img.onload = resolve;
            img.onerror = resolve;
        }));
    });

    await Promise.all(promises);
}

async function downloadReceiptPDF() {
    try {
        const { jsPDF } = window.jspdf;
        const receiptArea = document.getElementById('receipt-area');

        await waitForImages(receiptArea);

        const canvas = await html2canvas(receiptArea, {
            scale: 2,
            useCORS: true,
            backgroundColor: "#ffffff"
        });

        const imgData = canvas.toDataURL('image/png');

        const pdf = new jsPDF('p', 'mm', 'a4');
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();

        const margin = 8;
        const maxWidth = pageWidth - (margin * 2);
        const maxHeight = pageHeight - (margin * 2);

        let imgWidth = maxWidth;
        let imgHeight = (canvas.height * imgWidth) / canvas.width;

        if (imgHeight > maxHeight) {
            imgHeight = maxHeight;
            imgWidth = (canvas.width * imgHeight) / canvas.height;
        }

        const x = (pageWidth - imgWidth) / 2;
        const y = margin;

        pdf.addImage(imgData, 'PNG', x, y, imgWidth, imgHeight);
        pdf.save('recu-{{ transaction.reference }}.pdf');
    } catch (error) {
        console.error(error);
        alert("Erreur lors du téléchargement du reçu.");
    }
}
</script>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes transactions</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 0;
            padding-bottom: 40px;
        }

        .page {
            max-width: 520px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .simple-header {
            background: white;
            border-radius: 24px;
            padding: 22px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        .simple-header h1 {
            margin: 0;
            font-size: 28px;
            font-weight: bold;
            color: #111827;
        }

        .back-btn {
            display: inline-block;
            margin-top: 12px;
            background: #111827;
            color: white;
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            transition: 0.2s ease;
        }

        .back-btn:hover {
            background: #000;
            transform: translateY(-1px);
        }

        .card {
            background: white;
            border-radius: 24px;
            padding: 20px 16px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
        }

        .card h2 {
            margin: 0 0 16px 0;
            font-size: 22px;
            color: #111827;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            min-width: 700px;
        }

        th, td {
            padding: 14px 12px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
            font-size: 14px;
            vertical-align: middle;
        }

        th {
            background: #f8fafc;
            color: #111827;
            font-size: 13px;
            font-weight: bold;
        }

        tr:last-child td {
            border-bottom: none;
        }

        .tx-ref {
            font-weight: bold;
            color: #111827;
        }

        .tx-amount {
            font-weight: bold;
            color: #166534;
        }

        .status-badge {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            white-space: nowrap;
        }

        .success {
            background: #dcfce7;
            color: #166534;
        }

        .pending {
            background: #fef3c7;
            color: #92400e;
        }

        .failed {
            background: #fee2e2;
            color: #991b1b;
        }

        .view-btn {
            display: inline-block;
            background: #eff6ff;
            color: #1d4ed8;
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: bold;
            border: 1px solid #bfdbfe;
            transition: 0.2s ease;
        }

        .view-btn:hover {
            background: #dbeafe;
            transform: translateY(-1px);
        }

        .empty-box {
            text-align: center;
            padding: 28px 16px;
            color: #6b7280;
            line-height: 1.7;
        }

        @media (max-width: 520px) {
            .simple-header h1 {
                font-size: 24px;
            }

            .card h2 {
                font-size: 20px;
            }

            th, td {
                font-size: 13px;
                padding: 12px 10px;
            }

            .view-btn {
                font-size: 12px;
                padding: 7px 10px;
            }
        }
    </style>
</head>
<body>

<div class="page">
    <div class="simple-header">
        <h1>Mes transactions</h1>
        <a href="/admins/member-space/" class="back-btn">Retour à l’espace membre</a>
    </div>

    <div class="card">
        <h2>Historique des transactions</h2>

        <div class="table-wrap">
            <table>
                <tr>
                    <th>ID</th>
                    <th>Référence</th>
                    <th>Type</th>
                    <th>Montant</th>
                    <th>Statut</th>
                    <th>Date</th>
                    <th>Voir</th>
                </tr>

                {% for tx in transactions %}
                <tr>
                    <td>#{{ tx.id }}</td>
    <td class="tx-ref">{{ tx.reference }}</td>
    <td>{{ tx.transaction_type }}</td>
    <td class="tx-amount">{{ tx.amount }} FCFA</td>
                    <td>
                        {% if tx.status == 'success' %}
                            <span class="status-badge success">Succès</span>
                        {% elif tx.status == 'pending' %}
                            <span class="status-badge pending">En attente</span>
                        {% else %}
                            <span class="status-badge failed">Échoué</span>
                        {% endif %}
                    </td>
                    <td>{{ tx.created_at|date:"d/m/Y H:i" }}</td>
                    <td>
                        <a href="/admins/member-transaction/{{ tx.id }}/" class="view-btn">Voir</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="7">
                        <div class="empty-box">
                            Aucune transaction pour le moment.
                        </div>
                    </td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retrait</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 0;
            padding-bottom: 100px;
        }

        
        .simple-header {
    background: white;
    border-radius: 24px;
    padding: 22px 18px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    margin-bottom: 16px;
}

.simple-header h1 {
    margin: 0;
    font-size: 28px;
    font-weight: bold;
    color: #111827;
}

.back-btn {
    display: inline-block;
    margin-top: 12px;
    background: #111827;
    color: white;
    text-decoration: none;
    padding: 10px 16px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    transition: 0.2s ease;
}

.back-btn:hover {
    background: #000;
    transform: translateY(-1px);
}
       

.page {
    max-width: 520px;
    margin: 0 auto;
    padding: 18px 16px 0;
}

.info-card,
.form-card {
    background: white;
    border-radius: 24px;
    padding: 20px 16px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    margin-bottom: 16px;
}

.balance-box {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    border-radius: 20px;
    padding: 18px;
}

.balance-label {
    font-size: 13px;
    color: rgba(255,255,255,0.75);
    margin-bottom: 8px;
}

.balance-value {
    font-size: 30px;
    font-weight: bold;
}

.field {
    margin-bottom: 14px;
}

.field label {
    display: block;
    font-weight: bold;
    margin-bottom: 6px;
    color: #111827;
}

.field input,
.field textarea {
    width: 100%;
    padding: 13px 14px;
    border: 1px solid #d1d5db;
    border-radius: 14px;
    font-size: 15px;
    outline: none;
}

.field textarea {
    min-height: 100px;
    resize: vertical;
}

.submit-btn {
    width: 100%;
    border: none;
    background: #16a34a;
    color: white;
    padding: 14px 16px;
    border-radius: 14px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
}

.submit-btn:hover {
    background: #15803d;
}

.msg {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 14px;
    font-size: 14px;
    line-height: 1.6;
}

.msg-error {
    background: #fef2f2;
    color: #b91c1c;
    border: 1px solid #fecaca;
}

.msg-success {
    background: #f0fdf4;
    color: #166534;
    border: 1px solid #bbf7d0;
}

.warning-box {
    background: #fff7ed;
    border: 1px solid #fdba74;
    color: #9a3412;
    padding: 16px;
    border-radius: 16px;
    margin-bottom: 16px;
    font-size: 14px;
    line-height: 1.6;
}

.warning-box strong {
    display: block;
    margin-bottom: 8px;
    font-size: 15px;
}


    </style>
</head>
<body>

    

    <main class="page">

        <div class="simple-header">
    <h1>Retrait</h1>
    <a href="/admins/member-space/" class="back-btn"> Retour à l’espace membre</a>
    </div>

        


        


        <section class="info-card">
            <div class="balance-box">
                <div class="balance-label">Solde disponible</div>
                <div class="balance-value">{{ available_balance }} FCFA</div>
            </div>
        </section>


        <div class="warning-box">
    <strong>⚠️ Avertissement important</strong>
    <p>
        FondAction n’est pas seulement une plateforme, mais une communauté engagée vers des projets et avantages futurs destinés à ses membres. Ces opportunités vous seront communiquées en temps voulu.
        <br><br>
        Effectuer un retrait signifie réduire votre participation à cette dynamique collective.
        <br><br>
        Toute demande de retrait doit être faite avec sérieux.
        Une fois validée par l’administration, elle devient irréversible.
        <br><br>
        ⚠️ Toute demande inutile ou de test est fortement déconseillée :
        le montant pourra être prélevé sans garantie de transfert en cas d’erreur.
        <br><br>
        Avant de valider, assurez-vous que toutes les informations saisies sont correctes.
    </p>
</div>


        <section class="form-card">
            {% if error_message %}
                <div class="msg msg-error">{{ error_message }}</div>
            {% endif %}

            {% if success_message %}
                <div class="msg msg-success">{{ success_message }}</div>
            {% endif %}

            <form method="POST">
                {% csrf_token %}

                <div class="field">
                    <label>Montant</label>
                    <input type="number" name="amount" min="1" step="1" required>
                </div>

                <div class="field">
                    <label>Numéro qui va recevoir l'argent</label>
                    <input type="text" name="receiver_phone" required>
                </div>

                <div class="field">
                    <label>Motif</label>
                    <textarea name="reason" placeholder="Motif du retrait"></textarea>
                </div>

                <div class="field">
                    <label>Code PIN</label>
                    <input type="password" name="pin" maxlength="5" autocomplete="new-password" inputmode="numeric" required>
                </div>

                <button type="submit" class="submit-btn">Valider la demande</button>
            </form>
        </section>
    </main>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administration des membres</title>
    <style>
        * {
            box-sizing: border-box;
        }

        :root {
            --bg: #f3f6fb;
            --card: rgba(255, 255, 255, 0.95);
            --text: #0f172a;
            --muted: #64748b;
            --line: #e2e8f0;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --success: #16a34a;
            --danger: #dc2626;
            --purple: #7c3aed;
            --cyan: #0891b2;
            --orange: #d97706;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
            --radius-xl: 28px;
            --radius-lg: 22px;
            --radius-md: 16px;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
                linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
        }

        .page {
            max-width: 1320px;
            margin: 32px auto;
            padding: 20px;
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #2563eb 100%);
            color: white;
            border-radius: 32px;
            padding: 34px 32px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
        }

        .hero::before {
            content: "";
            position: absolute;
            top: -80px;
            right: -70px;
            width: 240px;
            height: 240px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .hero::after {
            content: "";
            position: absolute;
            bottom: -90px;
            left: -70px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: rgba(255,255,255,0.05);
        }

        .hero small {
            display: inline-block;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.82;
            margin-bottom: 12px;
        }

        .hero h1 {
            margin: 0 0 10px;
            font-size: 36px;
            line-height: 1.15;
            position: relative;
            z-index: 1;
        }

        .hero p {
            margin: 0;
            max-width: 850px;
            line-height: 1.7;
            color: rgba(255,255,255,0.88);
            position: relative;
            z-index: 1;
        }

        .hero-actions {
            margin-top: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            position: relative;
            z-index: 1;
        }

        .hero-btn,
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 14px;
            font-weight: bold;
            font-size: 14px;
            transition: 0.2s ease;
            border: none;
            cursor: pointer;
        }

        .hero-btn:hover,
        .btn:hover {
            transform: translateY(-1px);
        }

        .hero-btn-light {
            background: white;
            color: #0f172a;
        }

        .hero-btn-outline {
            background: rgba(255,255,255,0.12);
            color: white;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .section-card {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: var(--radius-xl);
            padding: 24px;
            box-shadow: var(--shadow);
            margin-bottom: 24px;
            backdrop-filter: blur(10px);
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }

        .section-head h2 {
            margin: 0 0 6px;
            font-size: 24px;
        }

        .section-head p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-box {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 20px;
            min-height: 120px;
        }

        .stat-box span {
            display: block;
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }

        .stat-box strong {
            display: block;
            font-size: 30px;
            line-height: 1.1;
            margin-bottom: 8px;
        }

        .stat-box p {
            margin: 0;
            color: var(--muted);
            font-size: 14px;
            line-height: 1.5;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(240px, 1fr));
            gap: 20px;
        }

        .card {
            display: block;
            text-decoration: none;
            color: var(--text);
            background: white;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
            border: 1px solid var(--line);
            transition: 0.22s ease;
            min-height: 210px;
            position: relative;
            overflow: hidden;
        }

        .card::after {
            content: "";
            position: absolute;
            right: -20px;
            top: -20px;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            opacity: 0.08;
            background: currentColor;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 18px 36px rgba(15, 23, 42, 0.10);
        }

        .card .icon {
            width: 58px;
            height: 58px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
            background: rgba(15, 23, 42, 0.06);
        }

        .card h3 {
            margin: 0 0 10px;
            font-size: 22px;
            line-height: 1.3;
        }

        .card p {
            margin: 0;
            color: var(--muted);
            line-height: 1.7;
            font-size: 14.5px;
        }

        .card-tag {
            display: inline-block;
            margin-top: 16px;
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
            background: #eff6ff;
            color: #1d4ed8;
        }

        .card-blue { color: var(--primary); }
        .card-green { color: var(--success); }
        .card-purple { color: var(--purple); }
        .card-cyan { color: var(--cyan); }
        .card-orange { color: var(--orange); }

        .bottom-actions {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        .btn-back {
            background: #e5e7eb;
            color: #111827;
        }

        .btn-logout {
            background: var(--danger);
            color: white;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-dark {
            background: #0f172a;
            color: white;
        }

        @media (max-width: 1100px) {
            .grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 760px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 24px 22px;
                border-radius: 24px;
            }

            .hero h1 {
                font-size: 28px;
            }

            .section-card {
                padding: 18px;
                border-radius: 22px;
            }

            .card {
                min-height: auto;
            }

            .hero-actions,
            .bottom-actions {
                flex-direction: column;
            }

            .hero-btn,
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="page">
        <div class="hero">
            <small>Administration • Espace membres</small>
            <h1>Administration des membres</h1>
            <p>
                Retrouvez ici toutes les actions liées à la gestion des membres :
                consultation, création, historique, exportation et accès rapide aux outils
                essentiels pour garder une interface élégante, claire et efficace.
            </p>

            <div class="hero-actions">
                <a href="/admins/dashboard/" class="hero-btn hero-btn-light">← Retour au dashboard</a>
                <a href="/admins/members/create/" class="hero-btn hero-btn-outline">📝 Enregistrer un membre</a>
            </div>
        </div>

        <div class="section-card">
            <div class="section-head">
                <div>
                    <h2>Pilotage rapide</h2>
                    <p>Accédez rapidement aux principaux modules liés à la gestion des membres.</p>
                </div>
            </div>

            <div class="stats-grid">
                <div class="stat-box">
                    <span>Consultation</span>
                    <strong>Membres</strong>
                    <p>Voir la liste des membres et accéder à leurs informations détaillées.</p>
                </div>

                <div class="stat-box">
                    <span>Enregistrement</span>
                    <strong>Création</strong>
                    <p>Ajouter rapidement de nouveaux membres dans le système.</p>
                </div>

                <div class="stat-box">
                    <span>Suivi</span>
                    <strong>Historique</strong>
                    <p>Contrôler les créations déjà effectuées et suivre l’activité.</p>
                </div>

                <div class="stat-box">
                    <span>Export</span>
                    <strong>Excel</strong>
                    <p>Télécharger les listes des membres pour traitement ou archivage.</p>
                </div>
            </div>

            <div class="grid">
                <a href="/admins/members/" class="card card-blue">
                    <div class="icon">📋</div>
                    <h3>Voir les membres</h3>
                    <p>Consulter la liste des membres enregistrés, accéder à leurs détails et suivre leur situation dans le système.</p>
                    <span class="card-tag">Consultation</span>
                </a>

                <a href="/admins/members/create/" class="card card-green">
                    <div class="icon">📝</div>
                    <h3>Enregistrer un membre</h3>
                    <p>Créer une nouvelle fiche membre avec toutes les informations personnelles, administratives et utiles au suivi.</p>
                    <span class="card-tag">Création rapide</span>
                </a>

                <a href="/admins/member-login/" class="card card-purple">
                    <div class="icon">🔐</div>
                    <h3>Connexion membre</h3>
                    <p>Accéder à l’interface de connexion dédiée aux membres pour tester ou vérifier leur parcours utilisateur.</p>
                    <span class="card-tag">Accès membre</span>
                </a>

                <a href="/admins/members/history/" class="card card-cyan">
                    <div class="icon">📜</div>
                    <h3>Historique de création</h3>
                    <p>Voir l’historique détaillé des membres enregistrés et suivre les actions déjà réalisées dans le temps.</p>
                    <span class="card-tag">Suivi</span>
                </a>

                <a href="/admins/members/export/" class="card card-orange">
                    <div class="icon">📤</div>
                    <h3>Exporter les membres</h3>
                    <p>Télécharger la liste des membres au format Excel pour archivage, contrôle, impression ou exploitation externe.</p>
                    <span class="card-tag">Export Excel</span>
                </a>
            </div>
        </div>

        <div class="section-card">
            <div class="section-head">
                <div>
                    <h2>Actions rapides</h2>
                    <p>Accès direct aux principales actions générales liées à cette section.</p>
                </div>
            </div>

            <div class="bottom-actions">
                <a href="/admins/dashboard/" class="btn btn-back">Retour au dashboard</a>
                <a href="/admins/members/" class="btn btn-primary">Voir les membres</a>
                <a href="/admins/members/export/" class="btn btn-dark">Exporter les membres</a>
                <a href="/admins/logout/" class="btn btn-logout">Se déconnecter</a>
                <a href="/admins/visiteur/" class="btn">Page visiteur</a>
            </div>
        </div>
    </div>
</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paiement membre</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 0;
            padding-bottom: 100px;
        }

        .page {
            max-width: 520px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .topbar {
            background: white;
            border-radius: 24px;
            padding: 22px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        
        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
            color: #111827;
        }

        .back-btn {
    display: inline-block;
    margin-top: 12px;

    background: #111827;
    color: white;
    text-decoration: none;

    padding: 10px 16px;
    border-radius: 10px;

    font-size: 14px;
    font-weight: 600;

    transition: 0.2s ease;
}

/* effet hover pro */
.back-btn:hover {
    background: #000;
    transform: translateY(-1px);
}

        .card {
            background: white;
            border-radius: 24px;
            padding: 20px 16px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
        }

        .card h2 {
            margin-top: 0;
            margin-bottom: 18px;
            color: #111827;
            font-size: 22px;
        }

        .member-box {
            margin-bottom: 18px;
            padding: 16px;
            background: #f8fafc;
            border-radius: 16px;
            color: #374151;
            line-height: 1.7;
            font-size: 15px;
            border: 1px solid #e5e7eb;
        }

        .alert-success {
            margin-bottom: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #dcfce7;
            color: #166534;
            font-weight: bold;
            font-size: 14px;
            line-height: 1.6;
        }

        .alert-error {
            margin-bottom: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #fee2e2;
            color: #991b1b;
            font-weight: bold;
            font-size: 14px;
            line-height: 1.6;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
            margin-bottom: 18px;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }

        th, td {
            padding: 14px 12px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
            font-size: 14px;
            vertical-align: top;
        }

        th {
            background: #f3f4f6;
            color: #111827;
            font-size: 13px;
        }

        tr:last-child td {
            border-bottom: none;
        }

        .amount {
            font-weight: bold;
            color: #166534;
            font-size: 16px;
        }

        .btn-submit {
            display: inline-block;
            width: 100%;
            border: none;
            background: #16a34a;
            color: white;
            padding: 14px 18px;
            border-radius: 14px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
        }

        .btn-submit:hover {
            opacity: 0.92;
        }

        .info-note {
            margin-top: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #eff6ff;
            color: #1e3a8a;
            line-height: 1.7;
            font-size: 14px;
        }

        .resume-box {
            margin-top: 14px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #f9fafb;
            color: #374151;
            line-height: 1.7;
            font-size: 14px;
            border: 1px solid #e5e7eb;
        }

        @media (max-width: 520px) {
            .topbar h1 {
                font-size: 24px;
            }

            .card h2 {
                font-size: 20px;
            }

            th, td {
                font-size: 13px;
                padding: 12px 10px;
            }

            .amount {
                font-size: 15px;
            }
        }
    </style>
</head>
<body>

    <div class="page">

    <div class="topbar">
    <h1>Paiement membre</h1>

    <a href="/admins/member-space/" class="back-btn">
         Retour à l’espace membre
    </a>
</div>

        <div class="card">
            <h2>Effectuer mon paiement</h2>

            {% if message %}
                <div class="alert-success">{{ message }}</div>
            {% endif %}

            {% if error %}
                <div class="alert-error">{{ error }}</div>
            {% endif %}

            <div class="member-box">
                <div><strong>Membre :</strong> {{ member.first_name }} {{ member.last_name }}</div>
                <div><strong>NIM :</strong> {{ member.nim }}</div>
                <div><strong>Téléphone :</strong> {{ member.phone }}</div>
            </div>

            <form method="POST" action="/admins/member-payment/start/">
                {% csrf_token %}

                <div class="table-wrap">
                    <table>
                        <tr>
                            <th>Libellé</th>
                            <th>Période</th>
                            <th>Montant</th>
                        </tr>
                        <tr>
                            <td>Paiement de cotisation mensuelle</td>
                            <td>{{ current_month_label }}</td>
                            <td class="amount">{{ amount }} FCFA</td>
                        </tr>
                    </table>
                </div>

                <button type="submit" class="btn-submit">Effectuer le paiement</button>
            </form>

            <div class="info-note">
                Le paiement affiché correspond automatiquement au mois en cours. Le montant mensuel est fixe et s'élève à <strong>1200,00 FCFA</strong>.
            </div>

            <div class="resume-box">
                Après validation, vous serez redirigé vers la plateforme de paiement sécurisée afin de finaliser votre cotisation mensuelle.
            </div>
        </div>
    </div>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retour paiement</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
        }

        .page {
            padding: 20px;
        }

        .card {
            background: white;
            border-radius: 16px;
            padding: 22px 18px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        }

        h1 {
            margin-top: 0;
            font-size: 22px;
            color: #111827;
        }

        .status {
            margin-top: 12px;
            font-weight: bold;
            font-size: 16px;
        }

        .success {
            color: #166534;
        }

        .pending {
            color: #92400e;
        }

        .failed {
            color: #991b1b;
        }

        .info {
            margin-top: 14px;
            color: #374151;
            line-height: 1.6;
            font-size: 14px;
        }

        .btn {
    display: block;
    width: 85%;              /* réduit la largeur */
    margin: 18px auto 0;     /* centre horizontalement */
    text-align: center;
    text-decoration: none;
    background: #2563eb;
    color: white;
    padding: 12px;
    border-radius: 12px;
    font-weight: bold;
}
    </style>
</head>

<body>

<div class="page">
    <div class="card">

        <h1>Retour de paiement</h1>

        {% if status == 'approved' %}
            <div class="status success"> Paiement validé avec succès</div>
        {% elif status == 'pending' %}
            <div class="status pending">⏳ Paiement en attente</div>
        {% else %}
            <div class="status failed"> Paiement non confirmé</div>
        {% endif %}

        <div class="info">
            <p><strong>Statut :</strong> {{ status }}</p>
            <p><strong>ID transaction :</strong> {{ transaction_id }}</p>
            <p>Vous pouvez retourner dans votre espace membre.</p>
        </div>

        <a href="/admins/member-space/" class="btn">
            Retour à l’espace membre
        </a>

    </div>
</div>

</body>
</html>




<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Politique de confidentialité - FondAction SARL</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #0f172a;
}

.page {
    min-height: 100vh;
    padding: 28px 26px 60px;
}

.topbar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 60px;
}

.back-btn {
    width: 54px;
    height: 54px;
    border: none;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.back-btn svg {
    width: 32px;
    height: 32px;
}

.content {
    max-width: 820px;
    margin: 0 auto;
}

.title {
    margin: 0;
    text-align: center;
    font-size: clamp(42px, 8vw, 76px);
    line-height: 1.08;
    font-weight: 900;
}

.title-line {
    width: 128px;
    height: 7px;
    border-radius: 999px;
    margin: 24px auto 58px;
    display: flex;
    overflow: hidden;
}

.title-line span { flex: 1; }
.line-green { background: #178a37; }
.line-yellow { background: #f59e0b; }
.line-red { background: #dc2626; }

.section {
    margin-bottom: 42px;
}

.section h2 {
    margin: 0 0 14px;
    color: #178a37;
    font-size: clamp(25px, 5vw, 38px);
    line-height: 1.2;
    font-weight: 900;
}

.section p,
.section li {
    color: #263244;
    font-size: clamp(20px, 4.4vw, 31px);
    line-height: 1.55;
    font-weight: 500;
}

.section p {
    margin: 0 0 18px;
}

ul {
    margin: 12px 0 0;
    padding-left: 28px;
}

strong {
    color: #0f172a;
    font-weight: 900;
}

@media (max-width: 600px) {
    .page { padding: 24px 22px 54px; }
    .topbar { margin-bottom: 52px; }
    .back-btn { width: 50px; height: 50px; }
}
</style>
</head>

<body>

<div class="page">
    <div class="topbar">
        <button class="back-btn" type="button" onclick="history.back()" aria-label="Retour">
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
            </svg>
        </button>
    </div>

    <main class="content">
        <h1 class="title">Politique de confidentialité</h1>

        <div class="title-line">
            <span class="line-green"></span>
            <span class="line-yellow"></span>
            <span class="line-red"></span>
        </div>

        <section class="section">
            <p>
                Chez <strong>FondAction SARL</strong>, la protection des données personnelles de nos membres est une priorité absolue.
                Nous nous engageons à assurer la confidentialité, la sécurité et la transparence dans la gestion de toutes les informations collectées.
            </p>
        </section>

        <section class="section">
            <h2>1. Informations collectées</h2>
            <p>Dans le cadre de l’inscription et de l’utilisation de nos services, nous pouvons collecter :</p>
            <ul>
                <li>Nom et prénom</li>
                <li>Numéro de téléphone</li>
                <li>Photo d’identification</li>
                <li>Données liées au compte membre</li>
                <li>Historique des contributions et activités</li>
            </ul>
        </section>

        <section class="section">
            <h2>2. Utilisation des données</h2>
            <p>
                Les données collectées servent à créer et gérer les comptes membres, sécuriser l’accès,
                faciliter les contributions, améliorer les services et communiquer avec les membres.
            </p>
            <p>
                Nous nous engageons à ne jamais utiliser vos données à des fins abusives ou non autorisées.
            </p>
        </section>

        <section class="section">
            <h2>3. Protection des données</h2>
            <p>
                FondAction SARL met en place des mesures de sécurité afin de protéger les informations personnelles
                contre l’accès non autorisé, la perte, la modification ou la divulgation.
            </p>
            <p>
                Seules les personnes autorisées peuvent accéder aux données dans le cadre strict de leurs fonctions.
            </p>
        </section>

        <section class="section">
            <h2>4. Partage des informations</h2>
            <p>
                FondAction SARL ne vend pas, n’échange pas et ne partage pas les données personnelles de ses membres
                avec des tiers sans consentement explicite, sauf obligation légale.
            </p>
        </section>

        <section class="section">
            <h2>5. Conservation des données</h2>
            <p>
                Les données sont conservées aussi longtemps que nécessaire pour assurer le bon fonctionnement du service
                et respecter les obligations légales applicables.
            </p>
        </section>

        <section class="section">
            <h2>6. Droits des membres</h2>
            <p>Chaque membre peut demander à accéder à ses informations, les modifier ou demander la suppression de son compte selon les conditions applicables.</p>
        </section>

        <section class="section">
            <h2>7. Transparence</h2>
            <p>
                FondAction repose sur un principe essentiel : <strong>la transparence totale</strong>.
                Chaque membre peut comprendre comment ses données sont utilisées et dans quel but.
            </p>
        </section>

        <section class="section">
            <h2>8. Contact</h2>
            <p>
                Pour toute question relative à la confidentialité ou à la gestion de vos données,
                vous pouvez contacter l’administration de FondAction via les canaux officiels.
            </p>
        </section>
    </main>
</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recherche de transactions</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 24px;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        .page {
            max-width: 1000px;
            margin: 0 auto;
        }

        .topbar {
            background: white;
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 18px;
        }

        .topbar h1 {
            margin: 0 0 10px 0;
        }

        .back-btn {
            display: inline-block;
            margin-top: 10px;
            background: #111827;
            color: white;
            text-decoration: none;
            padding: 10px 14px;
            border-radius: 10px;
            font-weight: bold;
        }

        .search-card,
        .result-card {
            background: white;
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 18px;
        }

        .search-form {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .search-form input {
            flex: 1;
            min-width: 260px;
            padding: 13px 14px;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            font-size: 15px;
        }

        .search-form button {
            border: none;
            background: #2563eb;
            color: white;
            padding: 13px 18px;
            border-radius: 12px;
            font-weight: bold;
            cursor: pointer;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        th, td {
            padding: 14px 12px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
            font-size: 14px;
        }

        th {
            background: #f8fafc;
        }

        .status {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .success {
            background: #dcfce7;
            color: #166534;
        }

        .pending {
            background: #fef3c7;
            color: #92400e;
        }

        .failed {
            background: #fee2e2;
            color: #991b1b;
        }

        .empty {
            color: #6b7280;
            line-height: 1.7;
        }
    </style>
</head>
<body>
<div class="page">
    <div class="topbar">
        <h1>Recherche de transactions</h1>
        <div>Recherchez une transaction à partir de son numéro de reçu.</div>
        <a href="/admins/admins-hub/" class="back-btn">Retour au hub admin</a>
    </div>

    <div class="search-card">
        <form method="GET" class="search-form">
            <input type="text" name="q" placeholder="Ex: RCPT-FAS-2026-00000025" value="{{ query }}">
            <button type="submit">Rechercher</button>
        </form>
    </div>

    <div class="result-card">
        {% if query %}
            {% if transactions %}
                <table>
                    <tr>
                        <th>Reçu</th>
                        <th>Référence</th>
                        <th>Membre</th>
                        <th>Montant</th>
                        <th>Statut</th>
                        <th>Date</th>
                    </tr>

                    {% for tx in transactions %}
                    <tr>
                        <td>{{ tx.receipt_number }}</td>
                        <td>{{ tx.reference }}</td>
                        <td>{{ tx.member.last_name }} {{ tx.member.first_name }}</td>
                        <td>{{ tx.amount }} FCFA</td>
                        <td>
                            {% if tx.status == 'success' %}
                                <span class="status success">Succès</span>
                            {% elif tx.status == 'pending' %}
                                <span class="status pending">En attente</span>
                            {% else %}
                                <span class="status failed">Échoué</span>
                            {% endif %}
                        </td>
                        <td>{{ tx.created_at|date:"d/m/Y H:i" }}</td>
                    </tr>
                    {% endfor %}
                </table>
            {% else %}
                <div class="empty">
                    Aucune transaction trouvée pour cette recherche.
                </div>
            {% endif %}
        {% else %}
            <div class="empty">
                Entrez un numéro de reçu pour lancer la recherche.
            </div>
        {% endif %}
    </div>
</div>
</body>
</html>



{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Inscription sécurisée - FondAction SARL</title>

<style>
* {
    box-sizing: border-box;
}

:root {
    --logo-size: 190px;       /* taille logo */
    --logo-x: 0px;            /* gauche (-) / droite (+) */
    --logo-y: 0px;            /* haut (-) / bas (+) */

    --close-size: 54px;       /* taille bouton fermer */
    --close-x: 0px;           /* gauche (-) / droite (+) */
    --close-y: 0px;           /* haut (-) / bas (+) */
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(180deg, #ffffff 0%, #f7fbf8 100%);
    color: #0f172a;
}

.page {
    min-height: 100vh;
    padding: 24px 26px 42px;
}

.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 36px;
}

.logo {
    width: var(--logo-size);
    height: auto;
    display: block;
    transform: translateX(var(--logo-x)) translateY(var(--logo-y));
}

.close-btn {
    width: var(--close-size);
    height: var(--close-size);
    border: none;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transform: translateX(var(--close-x)) translateY(var(--close-y));
}

.close-btn svg {
    width: 32px;
    height: 32px;
}

.hero {
    text-align: center;
    max-width: 760px;
    margin: 0 auto;
}

.security-icon {
    width: 142px;
    height: 142px;
    margin: 0 auto 22px;
    border-radius: 50%;
    background: #eef9f0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.security-icon svg {
    width: 78px;
    height: 78px;
}

.title {
    margin: 0;
    font-size: clamp(42px, 8vw, 72px);
    line-height: 1.05;
    font-weight: 900;
    color: #0f172a;
}

.title span {
    color: #178a37;
}

.title-line {
    width: 128px;
    height: 7px;
    border-radius: 999px;
    margin: 20px auto 28px;
    display: flex;
    overflow: hidden;
}

.title-line span {
    flex: 1;
}

.line-green {
    background: #178a37;
}

.line-yellow {
    background: #f59e0b;
}

.line-red {
    background: #dc2626;
}

.intro {
    margin: 0 auto;
    max-width: 720px;
    color: #263244;
    font-size: clamp(20px, 4.4vw, 31px);
    line-height: 1.45;
    font-weight: 500;
    text-align: left;
}

.intro strong {
    font-weight: 900;
    color: #0f172a;
}

.cards {
    max-width: 820px;
    margin: 42px auto 0;
    display: grid;
    gap: 20px;
}

.card {
    background: #ffffff;
    border: 1px solid #e8eef0;
    border-radius: 22px;
    padding: 24px;
    display: grid;
    grid-template-columns: 72px 1fr;
    gap: 22px;
    align-items: center;
    box-shadow: 0 12px 26px rgba(15, 23, 42, 0.06);
}

.card-icon {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: #eef9f0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card-icon svg {
    width: 42px;
    height: 42px;
}

.card-icon svg path {
    fill: #178a37;
    stroke: #178a37;
}

.card-content h3 {
    margin: 0 0 8px;
    color: #178a37;
    font-size: clamp(21px, 4.5vw, 30px);
    line-height: 1.2;
    font-weight: 900;
}

.card-content p {
    margin: 0;
    color: #263244;
    font-size: clamp(17px, 3.8vw, 24px);
    line-height: 1.4;
    font-weight: 500;
}

.agent-box {
    max-width: 820px;
    margin: 28px auto 0;
    padding: 24px;
    border-radius: 22px;
    border: 2px solid rgba(23, 138, 55, 0.28);
    background: rgba(23, 138, 55, 0.04);
    display: grid;
    grid-template-columns: 78px 1fr;
    gap: 22px;
    align-items: center;
}

.agent-icon {
    width: 78px;
    height: 78px;
    border-radius: 18px;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
}

.agent-icon svg {
    width: 50px;
    height: 50px;
}

.agent-text h3 {
    margin: 0 0 10px;
    color: #178a37;
    font-size: clamp(21px, 4.5vw, 30px);
    line-height: 1.25;
    font-weight: 900;
}

.agent-text p {
    margin: 0;
    color: #263244;
    font-size: clamp(17px, 3.8vw, 24px);
    line-height: 1.45;
}

.whatsapp-btn {
    max-width: 820px;
    min-height: 82px;
    margin: 30px auto 0;
    border-radius: 18px;
    background: #178a37;
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    font-size: clamp(22px, 4.8vw, 34px);
    font-weight: 900;
    box-shadow: 0 16px 30px rgba(23, 138, 55, 0.24);
}

.whatsapp-btn svg {
    width: 42px;
    height: 42px;
}

.whatsapp-btn svg path,
.whatsapp-btn svg .cls-1 {
    stroke: white;
}

.security-note {
    margin: 22px 0 0;
    text-align: center;
    color: #7b8794;
    font-size: 16px;
    font-weight: 700;
}

@media (max-width: 600px) {
    :root {
        --logo-size: 170px;   /* taille logo mobile */
        --logo-x: -18px;      /* gauche (-) / droite (+) mobile */
        --logo-y: 0px;        /* haut (-) / bas (+) mobile */

        --close-size: 50px;
        --close-x: 0px;
        --close-y: 0px;
    }

    .page {
        padding: 22px 20px 38px;
    }

    .header {
        margin-bottom: 30px;
    }

    .security-icon {
        width: 124px;
        height: 124px;
    }

    .security-icon svg {
        width: 68px;
        height: 68px;
    }

    .intro {
        text-align: left;
    }

    .card {
        grid-template-columns: 62px 1fr;
        gap: 18px;
        padding: 20px;
    }

    .card-icon {
        width: 62px;
        height: 62px;
    }

    .card-icon svg {
        width: 36px;
        height: 36px;
    }

    .agent-box {
        grid-template-columns: 64px 1fr;
        gap: 18px;
        padding: 20px;
    }

    .agent-icon {
        width: 64px;
        height: 64px;
    }

    .agent-icon svg {
        width: 42px;
        height: 42px;
    }

    .whatsapp-btn {
        min-height: 76px;
    }
}
</style>
</head>

<body>

<div class="page">

    <header class="header">
        <img src="{% static 'images/logo2.png' %}" alt="FondAction SARL" class="logo">

        <button class="close-btn" type="button" onclick="history.back()" aria-label="Retour">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
            </svg>
        </button>
    </header>

    <main class="hero">
        <div class="security-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.4901 2.23006L5.50015 4.10005C4.35015 4.53005 3.41016 5.89004 3.41016 7.12004V14.55C3.41016 15.73 4.19017 17.28 5.14017 17.99L9.44016 21.2001C10.8502 22.2601 13.1701 22.2601 14.5801 21.2001L18.8802 17.99C19.8302 17.28 20.6101 15.73 20.6101 14.55V7.12004C20.6101 5.89004 19.6701 4.53005 18.5201 4.10005L13.5302 2.23006C12.6802 1.92006 11.3201 1.92006 10.4901 2.23006Z" stroke="#178a37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                <path opacity="0.4" d="M11.9997 10.9199C11.9597 10.9199 11.9097 10.9199 11.8697 10.9199C10.9297 10.8899 10.1797 10.1099 10.1797 9.15991C10.1797 8.18991 10.9697 7.3999 11.9397 7.3999C12.9097 7.3999 13.6997 8.18991 13.6997 9.15991C13.6897 10.1199 12.9397 10.8899 11.9997 10.9199Z" stroke="#178a37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                <path opacity="0.4" d="M10.0091 13.7199C9.04906 14.3599 9.04906 15.4099 10.0091 16.0498C11.0991 16.7799 12.8891 16.7799 13.9791 16.0498C14.9391 15.4099 14.9391 14.3599 13.9791 13.7199C12.8991 12.9899 11.1091 12.9899 10.0091 13.7199Z" stroke="#178a37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>
        </div>

        <h1 class="title">Inscription <span>sécurisée</span></h1>
        <div class="title-line">
         <span class="line-green"></span>
         <span class="line-yellow"></span>
         <span class="line-red"></span>
        </div>

        <p class="intro">
            Pour garantir la sécurité de chaque membre et la fiabilité des informations enregistrées,
            <strong>l’inscription à FondAction se fait uniquement auprès d’un agent habilité ou d’un administrateur autorisé.</strong>
        </p>
    </main>

    <section class="cards">
        <div class="card">
            <div class="card-icon">
                <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                    <path d="M24,6.2c5.3,1.5,11.1,3.3,14,4.3V26.2c0,3.4-3.7,9.4-14,15.4-10.3-6.1-14-12-14-15.4V10.5c2.9-1.1,8.7-2.8,14-4.3M24,2S6,7.1,6,8V26.2c0,9.2,13.3,17.3,17,19.5a1.8,1.8,0,0,0,2,0c3.8-2.1,17-10.3,17-19.5V8c0-.9-18-6-18-6Z"></path>
                    <path d="M19.6,29.4l-5-4.9a2.1,2.1,0,0,1-.2-2.7,1.9,1.9,0,0,1,3-.2L21,25.2l9.6-9.6a2,2,0,0,1,2.8,2.8l-11,11A1.9,1.9,0,0,1,19.6,29.4Z"></path>
                </svg>
            </div>
            <div class="card-content">
                <h3>Vérification de votre identité</h3>
                <p>Chaque membre est authentifié pour garantir un environnement fiable et sécurisé.</p>
            </div>
        </div>

        <div class="card">
            <div class="card-icon">
                <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                    <path d="M316.16,438.479c0-28.392,12.205-53.92,31.551-71.838c-18.452-7.164-38.356-17.934-38.356-31.704 c0-9.533,0-21.444,0-37.782c6.996-19.393,17.51-20.781,22.768-50.546c12.254-4.379,19.258-11.384,28.009-42.026 c6.574-23.063-3.112-29.253-9.382-30.905c0.128-1.229,0.256-2.466,0.36-3.917c2.369-34.543,22.425-137.079-47.012-149.332 C285.717,6.134,274.054-0.343,234.66,2.05C209.723,2.042,190.768,7.546,164.354,0c-35.245,29.564-25.56,126.659-20.63,173.504 c-6.199,1.388-16.889,7.148-10.052,31.081c8.743,30.642,15.748,37.646,28.001,42.026c5.258,29.765,21.253,39.322,22.418,50.546 c0,16.338,0,28.248,0,37.782c0,14.4-23.494,26.55-40.877,32.676C109.78,379.397,16.634,414.276,24.795,512h324.766 C329.131,494.019,316.16,467.765,316.16,438.479z"></path>
                    <path d="M414.188,364.957c-40.606,0-73.521,32.916-73.521,73.522c0,40.606,32.916,73.521,73.521,73.521 c40.606,0,73.521-32.916,73.521-73.521C487.709,397.873,454.794,364.957,414.188,364.957z M455.033,448.69h-81.69v-20.423h81.69 V448.69z"></path>
                </svg>
            </div>
            <div class="card-content">
                <h3>Éviter les faux comptes</h3>
                <p>Notre procédure maintient une communauté de confiance et protège l’intégrité de la plateforme.</p>
            </div>
        </div>

        <div class="card">
            <div class="card-icon">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 14.5V16.5M7 10.0288C7.47142 10 8.05259 10 8.8 10H15.2C15.9474 10 16.5286 10 17 10.0288M7 10.0288C6.41168 10.0647 5.99429 10.1455 5.63803 10.327C5.07354 10.6146 4.6146 11.0735 4.32698 11.638C4 12.2798 4 13.1198 4 14.8V16.2C4 17.8802 4 18.7202 4.32698 19.362C4.6146 19.9265 5.07354 20.3854 5.63803 20.673C6.27976 21 7.11984 21 8.8 21H15.2C16.8802 21 17.7202 21 18.362 20.673C18.9265 20.3854 19.3854 19.9265 19.673 19.362C20 18.7202 20 17.8802 20 16.2V14.8C20 13.1198 20 12.2798 19.673 11.638C19.3854 11.0735 18.9265 10.6146 18.362 10.327C18.0057 10.1455 17.5883 10.0647 17 10.0288M7 10.0288V8C7 5.23858 9.23858 3 12 3C14.7614 3 17 5.23858 17 8V10.0288" stroke="#178a37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
            </div>
            <div class="card-content">
                <h3>Protection dès la création</h3>
                <p>Votre espace membre est protégé dès l’enrôlement pour assurer la sécurité de vos informations.</p>
            </div>
        </div>
    </section>

    <section class="agent-box">
        <div class="agent-icon">
            <svg viewBox="0 0 33.834 33.834" xmlns="http://www.w3.org/2000/svg">
                <path d="M32.253,29.334v4.5H1.581v-4.501c0-2.125,1.832-4.741,4.07-5.804l4.98-2.366l3.457,7.204l1.77-4.799 c0.349,0.066,0.695,0.154,1.059,0.154s0.709-0.088,1.059-0.154l1.68,4.563l3.389-7.048l5.141,2.445 C30.421,24.591,32.253,27.207,32.253,29.334z M6.105,13.562v-3.25c0-0.551,0.287-1.034,0.72-1.312c0.581-5.058,4.883-9,10.094-9 s9.514,3.942,10.096,9c0.432,0.278,0.719,0.761,0.719,1.312v3.25c0,0.863-0.699,1.563-1.563,1.563s-1.563-0.7-1.563-1.563v-0.683 c-0.846,4.255-3.961,8.205-7.688,8.205c-3.727,0-6.842-3.95-7.688-8.205v0.683c0,0.7-0.465,1.286-1.1,1.485 c0.622,2.117,2.002,3.946,3.908,5.146c0.352-0.116,0.796-0.094,1.227,0.13c0.692,0.36,1.045,1.06,0.783,1.56 c-0.261,0.5-1.033,0.612-1.729,0.251c-0.508-0.265-0.83-0.71-0.864-1.126c-2.183-1.396-3.731-3.533-4.37-5.998 C6.513,14.78,6.105,14.22,6.105,13.562z M7.89,8.635c0.047,0.003,0.092,0.004,0.137,0.021C8.14,8.698,8.222,8.779,8.279,8.874 c0.339,0.144,0.609,0.407,0.775,0.733C9.515,5.286,12.855,3,16.917,3c4.062,0,7.402,2.286,7.863,6.607 c0.229-0.449,0.664-0.77,1.185-0.837c-0.676-4.393-4.47-7.771-9.048-7.771C12.386,1,8.622,4.309,7.89,8.635z"></path>
            </svg>
        </div>

        <div class="agent-text">
            <h3>Finalisez votre enrôlement avec un agent FondAction</h3>
            <p>Veuillez cliquer en bas pour contacter l’administration et vous faire enrôler ou contacter l’un de nos agents.</p>
        </div>
    </section>

    <a href="https://wa.me/2290160212109" class="whatsapp-btn">
        <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <path class="cls-1" d="M24,2.5A21.52,21.52,0,0,0,5.15,34.36L2.5,45.5l11.14-2.65A21.5,21.5,0,1,0,24,2.5ZM13.25,12.27h5.86a1,1,0,0,1,1,1,10.4,10.4,0,0,0,.66,3.91,1.93,1.93,0,0,1-.66,2.44l-2.05,2a18.6,18.6,0,0,0,3.52,4.79A18.6,18.6,0,0,0,26.35,30l2-2.05c1-1,1.46-1,2.44-.66a10.4,10.4,0,0,0,3.91.66,1.05,1.05,0,0,1,1,1v5.86a1.05,1.05,0,0,1-1,1,23.68,23.68,0,0,1-15.64-6.84,23.6,23.6,0,0,1-6.84-15.64A1.07,1.07,0,0,1,13.25,12.27Z"></path>
        </svg>
        <span>Contacter FondAction</span>
    </a>

    <p class="security-note">Votre sécurité est notre priorité.</p>

</div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Termes et services - FondAction SARL</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #0f172a;
}

.page {
    min-height: 100vh;
    padding: 28px 26px 60px;
}

.topbar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 60px;
}

.back-btn {
    width: 54px;
    height: 54px;
    border: none;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.back-btn svg {
    width: 32px;
    height: 32px;
}

.content {
    max-width: 820px;
    margin: 0 auto;
}

.title {
    margin: 0;
    text-align: center;
    font-size: clamp(42px, 8vw, 76px);
    line-height: 1.08;
    font-weight: 900;
}

.title-line {
    width: 128px;
    height: 7px;
    border-radius: 999px;
    margin: 24px auto 58px;
    display: flex;
    overflow: hidden;
}

.title-line span { flex: 1; }
.line-green { background: #178a37; }
.line-yellow { background: #f59e0b; }
.line-red { background: #dc2626; }

.section {
    margin-bottom: 42px;
}

.section h2 {
    margin: 0 0 14px;
    color: #178a37;
    font-size: clamp(25px, 5vw, 38px);
    line-height: 1.2;
    font-weight: 900;
}

.section p,
.section li {
    color: #263244;
    font-size: clamp(20px, 4.4vw, 31px);
    line-height: 1.55;
    font-weight: 500;
}

.section p {
    margin: 0 0 18px;
}

ul {
    margin: 12px 0 0;
    padding-left: 28px;
}

strong {
    color: #0f172a;
    font-weight: 900;
}

@media (max-width: 600px) {
    .page { padding: 24px 22px 54px; }
    .topbar { margin-bottom: 52px; }
    .back-btn { width: 50px; height: 50px; }
}
</style>
</head>

<body>

<div class="page">
    <div class="topbar">
        <button class="back-btn" type="button" onclick="history.back()" aria-label="Retour">
            <svg viewBox="0 0 24 24" fill="none">
                <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
            </svg>
        </button>
    </div>

    <main class="content">
        <h1 class="title">Termes et services</h1>

        <div class="title-line">
            <span class="line-green"></span>
            <span class="line-yellow"></span>
            <span class="line-red"></span>
        </div>

        <section class="section">
            <p>
                Bienvenue sur la plateforme <strong>FondAction SARL</strong>.
                En accédant à nos services, vous acceptez les présentes conditions d’utilisation.
            </p>
        </section>

        <section class="section">
            <h2>1. Présentation</h2>
            <p>
                FondAction SARL est une initiative collective visant à regrouper les contributions des membres
                afin de financer des projets utiles, créer des opportunités et générer de la valeur à travers
                un système structuré, solidaire et transparent.
            </p>
        </section>

        <section class="section">
            <h2>2. Conditions d’inscription</h2>
            <p>
                L’inscription à FondAction est strictement encadrée afin de garantir la sécurité et l’authenticité du système.
            </p>
            <ul>
                <li>L’inscription se fait via un agent habilité ou l’administration</li>
                <li>Les informations fournies doivent être exactes et vérifiables</li>
                <li>Un seul compte est autorisé par personne</li>
            </ul>
        </section>

        <section class="section">
            <h2>3. Responsabilité du membre</h2>
            <p>
                Chaque membre est responsable de la confidentialité de ses informations d’accès,
                de l’utilisation correcte de son compte et du respect des règles établies par FondAction.
            </p>
        </section>

        <section class="section">
            <h2>4. Contributions et fonctionnement</h2>
            <p>
                Les contributions des membres constituent la base du système FondAction.
                Elles permettent de financer des projets collectifs, soutenir des initiatives utiles
                et développer des opportunités économiques.
            </p>
            <p>
                FondAction SARL s’engage à assurer une gestion responsable et transparente des ressources.
            </p>
        </section>

        <section class="section">
            <h2>5. Transparence du système</h2>
            <p>
                Toutes les opérations sont suivies et tracées afin de garantir une visibilité claire pour les membres.
                FondAction repose sur la confiance, la transparence et la responsabilité collective.
            </p>
        </section>

        <section class="section">
            <h2>6. Interdictions</h2>
            <p>Il est strictement interdit de :</p>
            <ul>
                <li>Créer de faux comptes</li>
                <li>Usurper l’identité d’une autre personne</li>
                <li>Manipuler ou tenter de détourner le système</li>
                <li>Utiliser la plateforme à des fins illégales</li>
            </ul>
        </section>

        <section class="section">
            <h2>7. Suspension ou suppression de compte</h2>
            <p>
                FondAction SARL se réserve le droit de suspendre ou supprimer un compte en cas de fraude,
                de fausse déclaration ou de non-respect des règles afin de protéger la communauté.
            </p>
        </section>

        <section class="section">
            <h2>8. Limitation de responsabilité</h2>
            <p>
                FondAction met tout en œuvre pour assurer un service fiable et sécurisé.
                Cependant, chaque utilisateur reste responsable de l’utilisation qu’il fait de la plateforme.
            </p>
        </section>

        <section class="section">
            <h2>9. Évolution des conditions</h2>
            <p>
                Les présentes conditions peuvent être modifiées afin d’améliorer le fonctionnement du système.
                Les membres seront informés des mises à jour importantes.
            </p>
        </section>

        <section class="section">
            <h2>10. Engagement</h2>
            <p>
                En rejoignant FondAction, vous devenez acteur d’un système collectif basé sur la confiance,
                la solidarité, la transparence et la création de valeur.
            </p>
        </section>
    </main>
</div>

</body>
</html>



{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>

<title>FondAction SARL - Contribution collective</title>

<meta name="description" content="FondAction SARL transforme les contributions en opportunités réelles pour ses membres au Bénin.">

<meta name="keywords" content="FondAction, contribution, investissement collectif, Bénin, épargne">

<meta name="robots" content="index, follow">

<meta property="og:title" content="FondAction SARL">
<meta property="og:description" content="Chaque contribution compte. Construisons ensemble.">
<meta property="og:url" content="https://fondactionsarl.com">
<meta property="og:type" content="website">
<meta property="og:image" content="https://fondactionsarl.com/static/images/logo2.png">


<link rel="icon" type="image/png" href="/static/images/favicon.png">

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">


<style>
* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
}

/* ===================== */
/* 🔧 RÉGLAGES DU LOGO */
/* ===================== */

:root {
    --logo-size: 120px;
    --logo-x: -50px;
    --logo-y: 0px;

    --menu-size: 44px;
    --menu-icon-size: 34px;
    --menu-x: 15px;
    --menu-y: 0px;

    --footer-logo-size: 350px;
    --footer-logo-x: 450px;
    --footer-logo-y: 0px;

    --header-height: 95px;
}

/* ===================== */

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #111827;
}

body.menu-open {
    overflow: hidden;
}

/* VRAI HEADER FIXE */
.site-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--header-height);
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(14px);
    z-index: 1000;
    transition: transform 0.28s ease, box-shadow 0.28s ease;
}

.site-header.hide {
    transform: translateY(-110%);
}

.site-header.show {
    transform: translateY(0);
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
}

.header-inner {
    height: 100%;
    padding: 0 26px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo-container {
    display: flex;
    align-items: center;
    transform: translateX(var(--logo-x)) translateY(var(--logo-y));
}

.logo {
    height: var(--logo-size);
    width: auto;
    object-fit: contain;
    display: block;
}

.menu-btn {
    width: var(--menu-size);
    height: var(--menu-size);
    border: none;
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transform: translateX(var(--menu-x)) translateY(var(--menu-y));
}

.menu-btn svg {
    width: var(--menu-icon-size);
    height: var(--menu-icon-size);
}

/* MENU PLEIN ÉCRAN */
.full-menu {
    position: fixed;
    inset: 0;
    background: #ffffff;
    z-index: 3000;
    transform: translateX(100%);
    opacity: 0;
    visibility: hidden;
    transition: transform 0.38s ease, opacity 0.25s ease, visibility 0.25s ease;
    overflow-x: hidden;
}

.full-menu.open {
    transform: translateX(0);
    opacity: 1;
    visibility: visible;
}

.full-menu-inner {
    min-height: 100vh;
    padding: 34px 26px 50px;
    display: flex;
    flex-direction: column;
}

.full-menu-top {
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

.close-menu-btn {
    width: 54px;
    height: 54px;
    border: none;
    border-radius: 999px;
    background: #f8fafc;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.close-menu-btn svg {
    width: 32px;
    height: 32px;
}

.full-menu-list {
    margin-top: 70px;
    display: grid;
    gap: 26px;
}

.full-menu-item {
    display: grid;
    grid-template-columns: 70px minmax(0, 1fr);
    align-items: center;
    gap: 24px;
    text-decoration: none;
    color: #20242c;
}

.full-menu-icon {
    width: 70px;
    height: 70px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.full-menu-icon svg {
    width: 34px;
    height: 34px;
}

.icon-blue { background: #eff6ff; }
.icon-green { background: #eefbea; }
.icon-orange { background: #fff3e5; }
.icon-purple { background: #f2edff; }
.icon-red { background: #fff1f2; }

.full-menu-text {
    min-width: 0;
    padding-bottom: 0;
    border-bottom: none;
    font-size: clamp(25px, 5vw, 34px);
    line-height: 1.1;
    font-weight: 900;
    display: flex;
    align-items: center;
    min-height: 70px;
    border-bottom: 1px solid #e5e7eb;
    overflow-wrap: break-word;
}

.full-menu-watermark {
    margin-top: auto;
    opacity: 0.035;
    text-align: center;
    font-size: 130px;
    font-weight: 900;
    color: #0f172a;
}

/* PAGE */
.page {
    width: 100%;
    max-width: 100%;
    min-height: 150vh;
    padding: calc(var(--header-height) + 38px) 26px 70px;
}

/* HERO */
.hero {
    max-width: 720px;
    width: 100%;
    margin: 0 auto;
    text-align: center;
}

.hero-title {
    margin: 0 auto;
    max-width: 100%;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(48px, 8vw, 88px);
    line-height: 1.08;
    font-weight: 900;
    text-align: center;
    overflow-wrap: break-word;
}

.green { color: #2f8f3a; }
.orange { color: #f19a00; }
.dark { color: #20242c; }

.subtitle {
    max-width: 650px;
    width: 100%;
    margin: 48px auto 0;
    color: #5f6b7a;
    font-size: clamp(22px, 4vw, 34px);
    line-height: 1.32;
    font-weight: 700;
    text-align: center;
    overflow-wrap: break-word;
}

/* BOUTONS */
.actions {
    margin-top: 70px;
    display: grid;
    gap: 24px;
}

.main-btn {
    width: 100%;
    min-height: 86px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    text-decoration: none;
    font-size: clamp(22px, 4vw, 34px);
    font-weight: 900;
    box-shadow: 0 12px 24px rgba(15, 23, 42, 0.14);
    padding: 0 14px;
    overflow-wrap: break-word;
}

.btn-login {
    background: #1684f7;
    color: white;
}

.btn-register {
    background: linear-gradient(135deg, #2f8f3a, #f19a00);
    color: white;
}

.btn-download {
    background: #ffffff;
    color: #1684f7;
    border: 3px solid #1684f7;
}

/* SECTIONS TEXTE */
.info-section {
    margin-top: 96px;
    padding: 58px 0;
    text-align: left;
}

.info-title {
    margin: 0 0 32px;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(42px, 7vw, 68px);
    line-height: 1;
    color: #cf002b;
    font-weight: 900;
    overflow-wrap: break-word;
}

.info-subtitle {
    margin: 0 0 18px;
    color: #5f6b7a;
    font-size: clamp(30px, 5vw, 48px);
    line-height: 1.28;
    font-weight: 900;
    overflow-wrap: break-word;
}

.info-text {
    margin: 0;
    color: #5f6b7a;
    font-size: clamp(25px, 4.4vw, 42px);
    line-height: 1.38;
    font-weight: 500;
    overflow-wrap: break-word;
}

/* CARROUSEL */
.carousel-section {
    margin-top: 60px;
}

.carousel-title {
    margin: 0 0 22px;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(38px, 6vw, 60px);
    color: #20242c;
    overflow-wrap: break-word;
}

.carousel-hint {
    margin: 0 0 22px;
    color: #5f6b7a;
    font-size: 18px;
    font-weight: 700;
}

.carousel {
    display: flex;
    gap: 18px;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    padding-bottom: 16px;
    scrollbar-width: none;
}

.carousel::-webkit-scrollbar {
    display: none;
}

.slide {
    flex: 0 0 86%;
    min-width: 0;
    scroll-snap-align: center;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 14px 30px rgba(15, 23, 42, 0.14);
    background: #f3f4f6;
    position: relative;
}

.slide img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    display: block;
}

.slide-overlay {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    padding: 24px 22px;
    color: #ffffff;
    background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.78) 100%);
}

.slide-overlay h3 {
    margin: 0 0 6px;
    font-size: 27px;
    line-height: 1.15;
    font-weight: 900;
}

.slide-overlay p {
    margin: 0;
    font-size: 16px;
    line-height: 1.4;
    font-weight: 700;
}

.dots {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 18px;
}

.dot {
    width: 13px;
    height: 13px;
    border-radius: 999px;
    background: #cbd5e1;
}

.dot.active {
    background: #1684f7;
}

/* LIGNE MULTICOLORE */
.color-line {
    width: 100vw;
    margin-left: calc(50% - 50vw);
    margin-top: 78px;
    height: 9px;
    display: flex;
}

.color-line div {
    flex: 1;
}

.line-green { background: #2f8f3a; }
.line-yellow { background: #facc15; }
.line-red { background: #dc2626; }

/* FOOTER */
.footer {
    padding: 64px 0 20px;
}

.footer-logo {
    width: var(--footer-logo-size);
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto 34px auto;
    transform: translateX(var(--footer-logo-x)) translateY(var(--footer-logo-y));
}

.footer-text {
    color: #5f6b7a;
    font-size: clamp(24px, 4vw, 36px);
    line-height: 1.45;
    font-weight: 500;
    margin: 0 0 60px;
    overflow-wrap: break-word;
}

.socials {
    display: flex;
    gap: 34px;
    align-items: center;
    margin-bottom: 70px;
    flex-wrap: wrap;
}

.social-link {
    width: 34px;
    height: 34px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #5f6b7a;
}

.social-link svg {
    width: 34px;
    height: 34px;
}

.social-link svg path,
.social-link svg rect,
.social-link svg circle {
    stroke: #5f6b7a;
    fill: none;
}

.social-link.facebook svg path,
.social-link.twitter svg path {
    fill: #5f6b7a;
    stroke: none;
}

.footer-group {
    margin-bottom: 56px;
}

.footer-heading {
    margin: 0 0 28px;
    color: #20242c;
    font-size: clamp(34px, 6vw, 48px);
    font-weight: 900;
    letter-spacing: 1px;
    overflow-wrap: break-word;
}

.footer-link {
    display: block;
    text-decoration: none;
    color: #5f6b7a;
    font-size: clamp(24px, 4vw, 36px);
    margin-bottom: 28px;
    font-weight: 500;
    overflow-wrap: break-word;
}

.footer-bottom {
    border-top: 1px solid #d1d5db;
    padding-top: 28px;
    margin-top: 20px;
}

.footer-copy {
    margin: 0;
    color: #5f6b7a;
    font-size: clamp(20px, 3.6vw, 30px);
    line-height: 1.45;
    font-weight: 500;
    overflow-wrap: break-word;
}

/* RESPONSIVE */
@media (max-width: 600px) {
    :root {
        --logo-size: 120px;
        --header-height: 86px;
        --logo-x: -50px;
        --logo-y: 0px;

        --menu-size: 44px;
        --menu-icon-size: 34px;
        --menu-x: 15px;
        --menu-y: 0px;

        --footer-logo-size: 350px;
        --footer-logo-x: 0px;
        --footer-logo-y: 0px;
    }

    .header-inner {
        padding: 0 22px;
    }

    .page {
        padding: calc(var(--header-height) + 36px) 22px 60px;
    }

    .hero {
        width: 100%;
        max-width: 100%;
        padding: 0;
    }

    .hero-title {
        font-size: clamp(40px, 11.5vw, 50px);
        line-height: 1.08;
        text-align: center;
        overflow-wrap: break-word;
    }

    .subtitle {
        width: 100%;
        max-width: 100%;
        padding: 0 8px;
        font-size: 22px;
        line-height: 1.34;
        text-align: center;
        overflow-wrap: break-word;
    }

    .main-btn {
        min-height: 82px;
        font-size: 24px;
        padding: 0 12px;
    }

    .info-section {
        margin-top: 86px;
    }

    .info-title {
        font-size: clamp(38px, 11vw, 56px);
    }

    .info-subtitle {
        font-size: clamp(27px, 8vw, 40px);
    }

    .info-text {
        font-size: clamp(23px, 6.6vw, 34px);
    }

    .carousel-title {
        font-size: clamp(34px, 10vw, 50px);
    }

    .slide {
        flex-basis: 88%;
    }

    .slide-overlay h3 {
        font-size: 25px;
    }

    .slide-overlay p {
        font-size: 15px;
    }

    .full-menu-inner {
        padding: 30px 22px 44px;
    }

    .full-menu-list {
        margin-top: 62px;
        gap: 24px;
    }

    .full-menu-item {
        grid-template-columns: 62px minmax(0, 1fr);
        gap: 18px;
        align-items: center;
    }

    .full-menu-icon {
        width: 62px;
        height: 62px;
    }

    .full-menu-icon svg {
        width: 31px;
        height: 31px;
    }

    .full-menu-text {
        min-height: 62px;
        font-size: 25px;
        line-height: 1.1;
        display: flex;
        align-items: center;
    }

    .full-menu-watermark {
        font-size: 92px;
    }

    .footer-logo {
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
}
</style></head>

<body>

<header class="site-header show" id="siteHeader">
    <div class="header-inner">
        <div class="logo-container">
            <img src="{% static 'images/logo2.png' %}" class="logo" alt="FondAction SARL">
        </div>

        <button class="menu-btn" type="button" aria-label="Menu" id="openMenuBtn">
            <svg viewBox="0 0 20 20">
                <path d="M2 5H18M2 10H18M2 15H18" stroke="#111" stroke-width="2" stroke-linecap="round"/>
            </svg>
        </button>
    </div>
</header>

<div class="full-menu" id="fullMenu">
    <div class="full-menu-inner">
        <div class="full-menu-top">
            <button class="close-menu-btn" type="button" aria-label="Fermer" id="closeMenuBtn">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                    <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                </svg>
            </button>
        </div>

        <div class="full-menu-list">
            <a href="/admins/member-login/" class="full-menu-item">
                <span class="full-menu-icon icon-blue">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10.49 2.23006L5.50003 4.10005C4.35003 4.53005 3.41003 5.89004 3.41003 7.12004V14.55C3.41003 15.73 4.19005 17.28 5.14005 17.99L9.44003 21.2001C10.85 22.2601 13.17 22.2601 14.58 21.2001L18.88 17.99C19.83 17.28 20.61 15.73 20.61 14.55V7.12004C20.61 5.89004 19.67 4.53005 18.52 4.10005L13.53 2.23006C12.68 1.92006 11.32 1.92006 10.49 2.23006Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M12.0001 10.92C11.9601 10.92 11.9101 10.92 11.8701 10.92C10.9301 10.89 10.1801 10.11 10.1801 9.16003C10.1801 8.19003 10.9701 7.40002 11.9401 7.40002C12.9101 7.40002 13.7001 8.19003 13.7001 9.16003C13.6901 10.12 12.9401 10.89 12.0001 10.92Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M10.01 13.72C9.05004 14.36 9.05004 15.41 10.01 16.05C11.1 16.78 12.89 16.78 13.98 16.05C14.94 15.41 14.94 14.36 13.98 13.72C12.9 12.99 11.11 12.99 10.01 13.72Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </span>
                <span class="full-menu-text">Connexion</span>
            </a>
            <a href="/admins/inscription-securisee/" class="full-menu-item">
                <span class="full-menu-icon icon-green">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M14.4399 19.05L15.9599 20.57L18.9999 17.53" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M12.16 10.87C12.06 10.86 11.94 10.86 11.83 10.87C9.44997 10.79 7.55997 8.84 7.55997 6.44C7.54997 3.99 9.53997 2 11.99 2C14.44 2 16.43 3.99 16.43 6.44C16.43 8.84 14.53 10.79 12.16 10.87Z" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M11.99 21.8101C10.17 21.8101 8.36004 21.3501 6.98004 20.4301C4.56004 18.8101 4.56004 16.1701 6.98004 14.5601C9.73004 12.7201 14.24 12.7201 16.99 14.5601" stroke="#292D32" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </span>
                <span class="full-menu-text">Inscription</span>
            </a>

            <a href="{% static 'documents/projet_fondaction.pdf' %}" class="full-menu-item">
                <span class="full-menu-icon icon-orange">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 7L12 14M12 14L15 11M12 14L9 11" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M16 17H12H8" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                        <path d="M22 12C22 16.714 22 19.0711 20.5355 20.5355C19.0711 22 16.714 22 12 22C7.28595 22 4.92893 22 3.46447 20.5355C2 19.0711 2 16.714 2 12C2 7.28595 2 4.92893 3.46447 3.46447C4.92893 2 7.28595 2 12 2C16.714 2 19.0711 2 20.5355 3.46447C21.5093 4.43821 21.8356 5.80655 21.9449 8" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"></path>
                    </svg>
                </span>
                <span class="full-menu-text">Télécharger le projet</span>
            </a>

            <a href="/admins/about/" class="full-menu-item">
                <span class="full-menu-icon icon-purple">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="11.9999" r="9" stroke="#292929" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"></circle>
                        <rect x="12" y="8" width="0.01" height="0.01" stroke="#292929" stroke-width="3.75" stroke-linejoin="round"></rect>
                        <path d="M12 12V16" stroke="#292929" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </span>
                <span class="full-menu-text">À propos</span>
            </a>

            <a href="/admins/contact/" class="full-menu-item">
                <span class="full-menu-icon icon-red">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M17.3545 22.2323C15.3344 21.7262 11.1989 20.2993 7.44976 16.5502C3.70065 12.8011 2.2738 8.66559 1.76767 6.6455C1.47681 5.48459 2.00058 4.36434 2.88869 3.72997L5.21694 2.06693C6.57922 1.09388 8.47432 1.42407 9.42724 2.80051L10.893 4.91776C11.5152 5.8165 11.3006 7.0483 10.4111 7.68365L9.24234 8.51849C9.41923 9.1951 9.96939 10.5846 11.6924 12.3076C13.4154 14.0306 14.8049 14.5807 15.4815 14.7576L16.3163 13.5888C16.9517 12.6994 18.1835 12.4847 19.0822 13.1069L21.1995 14.5727C22.5759 15.5257 22.9061 17.4207 21.933 18.783L20.27 21.1113C19.6356 21.9994 18.5154 22.5232 17.3545 22.2323ZM8.86397 15.136C12.2734 18.5454 16.0358 19.8401 17.8405 20.2923C18.1043 20.3583 18.4232 20.2558 18.6425 19.9488L20.3056 17.6205C20.6299 17.1665 20.5199 16.5348 20.061 16.2171L17.9438 14.7513L17.0479 16.0056C16.6818 16.5182 16.0047 16.9202 15.2163 16.7501C14.2323 16.5378 12.4133 15.8569 10.2782 13.7218C8.1431 11.5867 7.46219 9.7677 7.24987 8.7837C7.07977 7.9953 7.48181 7.31821 7.99439 6.95208L9.24864 6.05618L7.78285 3.93893C7.46521 3.48011 6.83351 3.37005 6.37942 3.6944L4.05117 5.35744C3.74413 5.57675 3.64162 5.89565 3.70771 6.15943C4.15989 7.96418 5.45459 11.7266 8.86397 15.136Z" fill="#0F0F0F"></path>
                    </svg>
                </span>
                <span class="full-menu-text">Contacte</span>
            </a>
        </div>

        <div class="full-menu-watermark">FAS</div>
    </div>
</div>

<div class="page">

    <main class="hero">
        <h1 class="hero-title">
            <span class="green">Ensemble, tout</span><br>
            <span class="orange">devient possible.</span><br>
            <span class="dark">Chaque contribution compte.</span>
        </h1>

        <p class="subtitle">
            FondAction transforme l’effort collectif en richesse partagée
            et en opportunités concrètes.
        </p>

        <div class="actions">
            <a href="/admins/member-login/" class="main-btn btn-login">CONNEXION</a>
            <a href="/admins/inscription-securisee/" class="main-btn btn-register">INSCRIPTION</a>
            <a href="{% static 'documents/projet_fondaction.pdf' %}" class="main-btn btn-download">TÉLÉCHARGER LE PROJET</a>
        </div>
    </main>

    <section class="info-section">
        <h2 class="info-title">Nos objectifs</h2>
        <h3 class="info-subtitle">
            Construire une force collective au service de chacun.
        </h3>
        <p class="info-text">
            FondAction rassemble les contributions des membres pour créer des opportunités concrètes,
            financer des projets utiles et bâtir un système solidaire capable de produire de la valeur pour tous.
        </p>
    </section>

    <section class="info-section">
        <h2 class="info-title">Nos visions</h2>
        <h3 class="info-subtitle">
            Une nouvelle manière de créer de la richesse ensemble.
        </h3>
        <p class="info-text">
            Nous voulons bâtir une communauté forte capable de financer ses propres projets,
            soutenir ses membres et transformer les contributions individuelles en opportunités collectives durables.
        </p>
    </section>

    <section class="info-section">
        <h2 class="info-title">La transparence</h2>
        <h3 class="info-subtitle">
            Une gestion claire, ouverte et vérifiable à tout moment.
        </h3>
        <p class="info-text">
            FondAction repose sur un principe simple : la confiance. Toutes les opérations,
            contributions et réalisations sont suivies, tracées et accessibles afin de garantir une visibilité totale.
            Rien n’est caché : chaque membre peut comprendre comment les ressources sont utilisées
            et voir concrètement les résultats obtenus.
        </p>
    </section>

    <section class="carousel-section">
        <h2 class="carousel-title">Un avenir prometteur</h2>
        <p class="carousel-hint">Glissez vers la droite pour découvrir →</p>

        <div class="carousel" id="carousel">
            <div class="slide">
                <img src="{% static 'images/carousel/solidarite.png' %}" alt="Solidarité">
                <div class="slide-overlay">
                    <h3>Solidarité</h3>
                    <p>Ensemble, nous sommes plus forts.</p>
                </div>
            </div>

            <div class="slide">
                <img src="{% static 'images/carousel/croissance.png' %}" alt="Croissance">
                <div class="slide-overlay">
                    <h3>Croissance</h3>
                    <p>Chaque contribution peut devenir une valeur durable.</p>
                </div>
            </div>

            <div class="slide">
                <img src="{% static 'images/carousel/construction.png' %}" alt="Construction">
                <div class="slide-overlay">
                    <h3>Construction</h3>
                    <p>Financer des projets utiles et bâtir du concret.</p>
                </div>
            </div>

            <div class="slide">
                <img src="{% static 'images/carousel/entrepreneur.png' %}" alt="Opportunités">
                <div class="slide-overlay">
                    <h3>Opportunités</h3>
                    <p>Soutenir les initiatives qui améliorent les vies.</p>
                </div>
            </div>

            <div class="slide">
                <img src="{% static 'images/carousel/vision.png' %}" alt="Vision d’avenir">
                <div class="slide-overlay">
                    <h3>Vision d’avenir</h3>
                    <p>Construire un futur prospère, inclusif et durable.</p>
                </div>
            </div>
        </div>

        <div class="dots">
            <span class="dot active"></span>
            <span class="dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
        </div>
    </section>

    <div class="color-line">
        <div class="line-green"></div>
        <div class="line-yellow"></div>
        <div class="line-red"></div>
    </div>

    <footer class="footer">
        <img src="{% static 'images/logo3.png' %}" alt="FondAction SARL" class="footer-logo">

        <p class="footer-text">
            FondAction SARL rassemble les forces individuelles pour créer des opportunités collectives,
            soutenir des projets utiles et bâtir une valeur durable pour tous.
        </p>

        <div class="socials">
            <!-- Tes icônes réseaux sociaux restent ici inchangées -->
        </div>

        <div class="footer-group">
            <h3 class="footer-heading">LÉGALE</h3>
            <a href="/admins/privacy-policy/" class="footer-link">Politique de confidentialité</a>
            <a href="/admins/terms-services/" class="footer-link">Termes et services</a>
        </div>

        <div class="footer-group">
            <h3 class="footer-heading">SOCIÉTÉ</h3>
            <a href="/admins/about/" class="footer-link">À propos</a>
            <a href="/admins/contact/" class="footer-link">Contact</a>
        </div>

        <div class="footer-bottom">
            <p class="footer-copy">© 2026 FondAction SARL. Tout droits réservés.</p>
        </div>
    </footer>

</div>

<script>
let lastScrollY = window.scrollY;
const header = document.getElementById("siteHeader");

window.addEventListener("scroll", function () {
    const currentScrollY = window.scrollY;

    if (currentScrollY <= 10) {
        header.classList.remove("hide");
        header.classList.add("show");
        lastScrollY = currentScrollY;
        return;
    }

    if (currentScrollY > lastScrollY) {
        header.classList.remove("show");
        header.classList.add("hide");
    } else {
        header.classList.remove("hide");
        header.classList.add("show");
    }

    lastScrollY = currentScrollY;
});

const carousel = document.getElementById("carousel");
const dots = document.querySelectorAll(".dot");

carousel.addEventListener("scroll", function () {
    const slides = document.querySelectorAll(".slide");
    let activeIndex = 0;
    let minDistance = Infinity;

    slides.forEach((slide, index) => {
        const distance = Math.abs(slide.getBoundingClientRect().left - carousel.getBoundingClientRect().left);
        if (distance < minDistance) {
            minDistance = distance;
            activeIndex = index;
        }
    });

    dots.forEach(dot => dot.classList.remove("active"));
    if (dots[activeIndex]) {
        dots[activeIndex].classList.add("active");
    }
});

const openMenuBtn = document.getElementById("openMenuBtn");
const closeMenuBtn = document.getElementById("closeMenuBtn");
const fullMenu = document.getElementById("fullMenu");

openMenuBtn.addEventListener("click", function () {
    fullMenu.classList.add("open");
    document.body.classList.add("menu-open");
});

closeMenuBtn.addEventListener("click", function () {
    fullMenu.classList.remove("open");
    document.body.classList.remove("menu-open");
});
</script>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demandes de retrait</title>
    <style>
        body {
            margin: 0;
            padding: 24px;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        h1 {
            margin-top: 0;
            margin-bottom: 20px;
        }

        .list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .card {
            background: white;
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
        }

        .row {
            margin-bottom: 8px;
            line-height: 1.6;
        }

        .actions {
            display: flex;
            gap: 10px;
            margin-top: 14px;
            flex-wrap: wrap;
        }

        .actions form {
            margin: 0;
        }

        .actions textarea {
            width: 260px;
            min-height: 70px;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 10px;
            resize: vertical;
        }

        .btn {
            border: none;
            border-radius: 12px;
            padding: 12px 16px;
            font-weight: bold;
            color: white;
            cursor: pointer;
        }

        .btn-green {
            background: #16a34a;
        }

        .btn-red {
            background: #dc2626;
        }

        .status {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }

        .pending {
            background: #fef3c7;
            color: #92400e;
        }

        .approved {
            background: #dcfce7;
            color: #166534;
        }

        .rejected {
            background: #fee2e2;
            color: #991b1b;
        }
    </style>
</head>
<body>

    <h1>Demandes de retrait</h1>

    <div class="list">
        {% for item in requests_list %}
            <div class="card">
                <div class="row"><strong>Membre :</strong> {{ item.member.last_name }} {{ item.member.first_name }}</div>
                <div class="row"><strong>NIM :</strong> {{ item.member.nim }}</div>
                <div class="row"><strong>Montant :</strong> {{ item.amount }} FCFA</div>
                <div class="row"><strong>Numéro destinataire :</strong> {{ item.receiver_phone }}</div>
                <div class="row"><strong>Motif :</strong> {{ item.reason|default:"—" }}</div>
                <div class="row"><strong>Date :</strong> {{ item.created_at|date:"d/m/Y H:i" }}</div>
                <div class="row">
                    <strong>Statut :</strong>
                    <span class="status {{ item.status }}">{{ item.status }}</span>
                </div>

                {% if item.status == 'pending' %}
                    <div class="actions">
                        <form method="POST" action="/admins/withdrawal-requests/{{ item.id }}/approve/">
                            {% csrf_token %}
                            <textarea name="admin_note" placeholder="Note admin (optionnelle)"></textarea><br>
                            <button type="submit" class="btn btn-green">Valider</button>
                        </form>

                        <form method="POST" action="/admins/withdrawal-requests/{{ item.id }}/reject/">
                            {% csrf_token %}
                            <textarea name="admin_note" placeholder="Raison du refus (optionnelle)"></textarea><br>
                            <button type="submit" class="btn btn-red">Refuser</button>
                        </form>
                    </div>
                {% endif %}
            </div>
        {% empty %}
            <div class="card">
                Aucune demande de retrait pour le moment.
            </div>
        {% endfor %}
    </div>

</body>
</html>


import json

import hmac
import hashlib
import time
from django.conf import settings
import logging


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password

from admins.models import AdminUser
from members.models import Member, FedapayPaymentAttempt
from admins.utils import log_activity
from members.constants import (
    
    ADMIN_STATUS_ACTIVE,
    ADMIN_STATUS_SUSPENDED,
    
)
from members.payment_services import process_fedapay_webhook
from members.services import create_member_record

logger = logging.getLogger(__name__)



def api_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'OPTIONS':
            return cors_json_response({'success': True})

        admin_id = request.session.get('admin_id')
        if not admin_id:
            return cors_json_response({
                'success': False,
                'message': 'Admin non authentifié'
            }, status=401)

        return view_func(request, *args, **kwargs)
    return wrapper


def cors_json_response(data, status=200):
    return JsonResponse(data, status=status)

@csrf_exempt
def api_login(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''

    if not email or not password:
        return cors_json_response({
            'success': False,
            'message': 'Email et mot de passe obligatoires'
        }, status=400)

    try:
        user = AdminUser.objects.get(email=email)

        if user.is_locked:
            return cors_json_response({
                'success': False,
                'message': 'Compte admin bloqué ❌'
            }, status=403)

        if user.status == ADMIN_STATUS_SUSPENDED:
            return cors_json_response({
                'success': False,
                'message': 'Compte suspendu ❌'
            }, status=403)

        if user.status != ADMIN_STATUS_ACTIVE:
            return cors_json_response({
                'success': False,
                'message': 'Compte inactif ❌'
            }, status=403)

        if not check_password(password, user.password):
            user.failed_login_attempts += 1

            if user.failed_login_attempts >= 5:
                user.is_locked = True
                user.save(update_fields=['failed_login_attempts', 'is_locked', 'updated_at'])
                return cors_json_response({
                    'success': False,
                    'message': 'Compte admin bloqué après plusieurs tentatives ❌'
                }, status=403)

            user.save(update_fields=['failed_login_attempts', 'updated_at'])
            remaining = 5 - user.failed_login_attempts

            return cors_json_response({
                'success': False,
                'message': f'Mot de passe incorrect ❌ Il reste {remaining} tentative(s).'
            }, status=401)

        user.failed_login_attempts = 0
        user.save(update_fields=['failed_login_attempts', 'updated_at'])

        request.session['admin_id'] = user.id
        request.session['admin_role'] = user.role
        request.session['admin_email'] = user.email

        log_activity(
            admin_user=user,
            action='login',
            target_type='admin',
            target_id=user.id,
            details=f"{user.email} s’est connecté via mobile"
        )

        return cors_json_response({
            'success': True,
            'message': 'Connexion réussie ✅',
            'must_change_password': user.must_change_password,
            'admin': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'role': user.role,
                'status': user.status,
            }
        })

    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Utilisateur introuvable ❌'
        }, status=404)


@csrf_exempt
@api_admin_required
def api_change_admin_password(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Admin introuvable'
        }, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if not new_password or not confirm_password:
        return cors_json_response({
            'success': False,
            'message': 'Les deux champs sont obligatoires'
        }, status=400)

    if len(new_password) < 6:
        return cors_json_response({
            'success': False,
            'message': 'Le mot de passe doit contenir au moins 6 caractères'
        }, status=400)

    if new_password != confirm_password:
        return cors_json_response({
            'success': False,
            'message': 'Les deux mots de passe ne correspondent pas'
        }, status=400)

    admin.password = make_password(new_password)
    admin.must_change_password = False
    admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

    log_activity(
        admin_user=admin,
        action='change_admin_password',
        target_type='admin',
        target_id=admin.id,
        details=f"{admin.email} a changé son mot de passe via mobile"
    )

    return cors_json_response({
        'success': True,
        'message': 'Mot de passe changé avec succès ✅'
    })



@csrf_exempt
@api_admin_required
def api_create_member(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        current_admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Admin introuvable'
        }, status=404)

    signature = request.FILES.get('signature')
    if signature and not signature.name.lower().endswith('.png'):
        return cors_json_response({
            'success': False,
            'message': 'La signature doit être en format PNG'
        }, status=400)

    try:
        member = create_member_record(request.POST, request.FILES, current_admin)
    except ValueError as e:
        return cors_json_response({
            'success': False,
            'message': str(e)
        }, status=400)
    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur serveur'
        }, status=500)

    log_activity(
        admin_user=current_admin,
        action='create_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a créé le membre {member.nim}"
    )

    return cors_json_response({
        'success': True,
        'message': 'Membre enregistré avec succès ✅',
        'member': {
            'id': member.id,
            'nim': member.nim,
            'first_name': member.first_name,
            'last_name': member.last_name,
            'phone': member.phone,
            'id_card_type': member.id_card_type,
            'status': member.status,
            'created_at': member.created_at.isoformat(),
        }
    }, status=201)

@api_admin_required
def api_member_history(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'GET':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        members = Member.objects.filter(
            created_by_id=admin_id
        ).order_by('-created_at')

        members_data = []
        for member in members:
            members_data.append({
                'id': member.id,
                'nim': member.nim,
                'first_name': member.first_name,
                'last_name': member.last_name,
                'phone': member.phone or '',
                'created_at': member.created_at.isoformat(),
            })

        return cors_json_response({
            'success': True,
            'members': members_data,
        })

    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur serveur'
        }, status=500)

@api_admin_required
def api_get_member_by_nim(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'GET':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Non authentifié'
        }, status=401)

    nim = (request.GET.get('nim') or '').strip()

    if not nim:
        return cors_json_response({
            'success': False,
            'message': 'NIM manquant'
        }, status=400)

    try:
        member = Member.objects.filter(nim__iexact=nim.strip()).first()

        if not member:
            return cors_json_response({
                 'success': False,
                 'message': 'Membre introuvable'
            }, status=404)
        return cors_json_response({
            'success': True,
            'member': {
                'nim': member.nim,
                'first_name': member.first_name,
                'last_name': member.last_name,
                'phone': member.phone or '',
            }
        })
    except Member.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Membre introuvable'
        }, status=404)


def verify_fedapay_signature(raw_body: bytes, signature_header: str) -> bool:
    secret = settings.FEDAPAY_WEBHOOK_SECRET

    if not secret:
        return False

    if not signature_header:
        return False

    parts = {}
    for item in signature_header.split(','):
        if '=' in item:
            k, v = item.split('=', 1)
            parts[k.strip()] = v.strip()

    timestamp = parts.get('t')
    received_signature = parts.get('s')

    if not timestamp or not received_signature:
        return False

    try:
        int(timestamp)
    except ValueError:
        return False

    signed_payload = f"{timestamp}.".encode("utf-8") + raw_body

    expected_signature = hmac.new(
        secret.encode("utf-8"),
        signed_payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, received_signature)


@csrf_exempt
def fedapay_webhook(request):
    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    content_type = request.headers.get('Content-Type', '')
    if 'application/json' not in content_type:
        return cors_json_response({
            'success': False,
            'message': 'Content-Type invalide'
        }, status=400)

    signature = request.headers.get('X-FEDAPAY-SIGNATURE', '')
    raw_body = request.body


    if not signature:
        return cors_json_response({
            'success': False,
            'message': 'Signature webhook manquante'
        }, status=400)

    try:
        if not verify_fedapay_signature(raw_body, signature):
            return cors_json_response({
                'success': False,
                'message': 'Signature webhook invalide'
            }, status=400)
    except Exception:
       logger.exception("Erreur lors de la vérification de la signature FedaPay")
       return cors_json_response({
        'success': False,
        'message': 'Erreur vérification signature'
    }, status=400)

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    event_name = payload.get('name') or payload.get('event')
    allowed_events = {
        'transaction.approved',
        'transaction.declined',
        'transaction.created',
        'transaction.canceled',
        'transaction.cancelled',
    }

    if event_name and event_name not in allowed_events:
        return cors_json_response({
            'success': True,
            'message': 'Événement ignoré'
        })

    try:
        result = process_fedapay_webhook(payload)

        messages = {
            'declined': 'Paiement refusé',
            'pending': 'Paiement en attente',
            'already_processed': 'Paiement déjà enregistré',
            'approved': 'Paiement confirmé et enregistré',
        }

        return cors_json_response({
            'success': True,
            'message': messages.get(result, 'Traitement terminé')
        })

    except FedapayPaymentAttempt.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Tentative de paiement introuvable'
        }, status=404)

    except Exception:
     logger.exception("Erreur lors du traitement du webhook FedaPay")
     return cors_json_response({
        'success': False,
        'message': 'Erreur webhook'
    }, status=500)




from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect


def admin_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


def super_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        if request.session.get('admin_role') != 'super_admin':
            return HttpResponse("Accès refusé ❌")
        return view_func(request, *args, **kwargs)
    return wrapper


def member_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('member_id'):
            return redirect('/admins/member-login/')
        return view_func(request, *args, **kwargs)
    return wrapper



from django.db import models


class AdminUser(models.Model):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
    ]

    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('suspended', 'Suspendu'),
        ('inactive', 'Inactif'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    nim = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='admin')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    must_change_password = models.BooleanField(default=False)
    failed_login_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email




from django.urls import path

from .web_views import (
    home,
    login,
    change_admin_password,
    dashboard,
    members_hub,
    admins_hub,
    admin_list,
    create_admin,
    admin_detail,
    reset_admin_password,
    admin_performance_detail,
    export_admin_performance_excel,
    suspend_admin,
    reactivate_admin,
    activity_logs,
    create_member,
    member_list,
    member_detail,
    member_login,
    member_space,
    member_logout,
    logout,
    reset_member_pin,
    member_change_pin,
    member_card,
    download_member_card_pdf,
    edit_member,
    suspend_member,
    activate_member,
    member_creation_history,
    export_members_excel,
    export_admins_excel,
    member_payment,
    start_member_payment,
    payment_return,
    member_transactions,
    info_post_list,
    create_info_post,
    member_info_posts,
    edit_info_post,
    delete_info_post,
    member_profile,
    member_settings,
    member_withdrawal,
    withdrawal_requests,
    approve_withdrawal,
    reject_withdrawal,
    member_transaction_detail,
    search_transactions,
    member_assistance,
    global_admin_performance,
    export_global_admin_performance_excel,
    export_admins_summary_excel,
    visitor_home,
    secure_registration_page,
    about_page,
    privacy_policy_page,
    terms_services_page,
    contact_page,
    root_router,
    robots_txt,

)

from .api_views import (
    api_login,
    api_change_admin_password,
    api_create_member,
    api_member_history,
    api_get_member_by_nim,
    fedapay_webhook,

)

urlpatterns = [
    path('', home),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
    path('members-hub/', members_hub),
    path('admins-hub/', admins_hub),

    path('list/', admin_list),
    path('create/', create_admin),
    path('api/member-by-nim/', api_get_member_by_nim, name='api_member_by_nim'),
    path('change-password/', change_admin_password),

    path('admins/<int:admin_id>/', admin_detail),
    path('admins/<int:admin_id>/reset-password/', reset_admin_password),
    path('admins/<int:admin_id>/performance/', admin_performance_detail),
    path('admins/<int:admin_id>/performance/export/', export_admin_performance_excel),

    path('suspend/<int:admin_id>/', suspend_admin),
    path('reactivate/<int:admin_id>/', reactivate_admin),

    path('logs/', activity_logs),

    path('members/', member_list),
    path('members/create/', create_member),
    path('members/<int:member_id>/', member_detail),
    path('members/<int:member_id>/edit/', edit_member),
    path('members/<int:member_id>/suspend/', suspend_member),
    path('members/<int:member_id>/activate/', activate_member),
    path('members/<int:member_id>/reset-pin/', reset_member_pin),
    path('members/history/', member_creation_history),
    path('members/export/', export_members_excel),

    path('admins/export/', export_admins_excel),

    path('member-login/', member_login),
    path('member-space/', member_space),
    path('member-logout/', member_logout),
    path('member-change-pin/', member_change_pin),
    path('member-card/', member_card),
    path('member-card/download-pdf/', download_member_card_pdf),
    path('member-payment/', member_payment),
    path('member-payment/start/', start_member_payment),
    path('payment-return/', payment_return),
    path('member-transactions/', member_transactions),

    path('api/login/', api_login, name='api_login'),
    path('api/change-password/', api_change_admin_password, name='api_change_admin_password'),
    path('api/members/create/', api_create_member, name='api_create_member'),
    path('api/members/history/', api_member_history, name='api_member_history'),
    path('api/fedapay/webhook/', fedapay_webhook, name='fedapay_webhook'),
    path('info-posts/', info_post_list),
    path('info-posts/create/', create_info_post),
    path('info-posts/<int:post_id>/edit/', edit_info_post),
    path('info-posts/<int:post_id>/delete/', delete_info_post),
    path('member-infos/', member_info_posts),
    path('member-profile/', member_profile),
    path('member-settings/', member_settings),
    path('member-withdrawal/', member_withdrawal),
    path('withdrawal-requests/', withdrawal_requests),
    path('withdrawal-requests/<int:withdrawal_id>/approve/', approve_withdrawal),
    path('withdrawal-requests/<int:withdrawal_id>/reject/', reject_withdrawal),
    path('member-transaction/<int:transaction_id>/', member_transaction_detail),
    path('search-transactions/', search_transactions),
    path('member-assistance/', member_assistance),
    path('admins/performance/', global_admin_performance),
    path('admins/performance/export/', export_global_admin_performance_excel),
    path('admins/performance/admins-summary/export/', export_admins_summary_excel),
    path('visiteur/', visitor_home, name='visitor_home'),
    path('inscription-securisee/', secure_registration_page, name='secure_registration_page'),
    path('about/', about_page, name='about_page'),
    path('privacy-policy/', privacy_policy_page, name='privacy_policy_page'),
    path('terms-services/', terms_services_page, name='terms_services_page'),
    path('contact/', contact_page, name='contact_page'),
    path('', root_router),
    path('robots.txt', robots_txt),

]



import secrets
import string

from logs.models import ActivityLog


def log_activity(admin_user, action, target_type=None, target_id=None, details=None, status='success'):
    ActivityLog.objects.create(
        admin_user=admin_user,
        action=action,
        target_type=target_type,
        target_id=target_id,
        details=details,
        status=status
    )


def generate_temporary_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def generate_temporary_pin(length=5):
    digits = string.digits
    return ''.join(secrets.choice(digits) for _ in range(length))




import openpyxl
from io import BytesIO
from datetime import timedelta
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings

from django.db.models import Exists, OuterRef, Sum,  Q

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.template.loader import get_template
from django.utils import timezone
from xhtml2pdf import pisa
from members.models import InfoPost
from django.shortcuts import get_object_or_404
from admins.models import AdminUser
from members.models import Member, MemberTransaction, WithdrawalRequest
from admins.utils import (
    log_activity,
    generate_temporary_password,
    generate_temporary_pin,
)
from admins.decorators import (
    admin_session_required,
    super_admin_required,
    member_session_required,
)


from members.services import (
    get_total_contributions,
    get_available_balance,
    get_recent_transactions,
    create_withdrawal_request,
    approve_withdrawal_request,
    reject_withdrawal_request,
)


from members.permissions import forbid_if_no_member_access
from members.constants import (
    DEFAULT_MONTHLY_CONTRIBUTION,
    DEFAULT_PAYMENT_MONTHS,
    MEMBER_STATUS_ACTIVE,
    MEMBER_STATUS_SUSPENDED,
    ADMIN_STATUS_ACTIVE,
    ADMIN_STATUS_SUSPENDED,
    MAX_MEMBER_PIN_ATTEMPTS,
)
from members.payment_services import start_fedapay_payment
from members.services import create_member_record, validate_uploaded_image


def home(request):
    if request.session.get('admin_id'):
        return redirect('/admins/dashboard/')

    if request.session.get('member_id'):
        return redirect('/admins/member-space/')

    return redirect('/admins/login/')


def login(request):
    if request.method == 'POST':


        if is_rate_limited(
            request,
            key_prefix='admin_login',
            max_attempts=settings.LOGIN_RATE_LIMIT_MAX_ATTEMPTS,
            window_seconds=settings.LOGIN_RATE_LIMIT_WINDOW_SECONDS
        ):
            return HttpResponse("Trop de tentatives. Veuillez réessayer dans 10 minutes.")

        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password') or ''

        try:
            user = AdminUser.objects.get(email=email)

            if user.is_locked:
                return HttpResponse("Compte admin bloqué ❌")

            if user.status == ADMIN_STATUS_SUSPENDED:
                return HttpResponse("Compte suspendu ❌")

            if user.status != ADMIN_STATUS_ACTIVE:
                return HttpResponse("Compte inactif ❌")

            if not check_password(password, user.password):
                user.failed_login_attempts += 1

                if user.failed_login_attempts >= 5:
                    user.is_locked = True
                    user.save(update_fields=['failed_login_attempts', 'is_locked', 'updated_at'])
                    return HttpResponse("Compte admin bloqué après plusieurs tentatives ❌")

                user.save(update_fields=['failed_login_attempts', 'updated_at'])
                remaining = 5 - user.failed_login_attempts
                return HttpResponse(f"Mot de passe incorrect ❌ Il reste {remaining} tentative(s).")

            user.failed_login_attempts = 0
            user.save(update_fields=['failed_login_attempts', 'updated_at'])

            request.session['admin_id'] = user.id
            request.session['admin_role'] = user.role
            request.session['admin_email'] = user.email

            log_activity(
                admin_user=user,
                action='login',
                target_type='admin',
                target_id=user.id,
                details=f"{user.email} s’est connecté"
            )

            if user.must_change_password:
                return redirect('/admins/change-password/')

            return redirect('/admins/dashboard/')

        except AdminUser.DoesNotExist:
            return HttpResponse("Utilisateur introuvable ❌")

    return render(request, 'admins/login.html')




@admin_session_required
def logout(request):
    request.session.flush()
    return redirect('/admins/login/')


@admin_session_required
def change_admin_password(request):
    try:
        admin = AdminUser.objects.get(id=request.session.get('admin_id'))
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not new_password or len(new_password) < 6:
            return HttpResponse("Le nouveau mot de passe doit contenir au moins 6 caractères ❌")

        if new_password != confirm_password:
            return HttpResponse("Les deux mots de passe ne correspondent pas ❌")

        admin.password = make_password(new_password)
        admin.must_change_password = False
        admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

        log_activity(
            admin_user=admin,
            action='change_admin_password',
            target_type='admin',
            target_id=admin.id,
            details=f"{admin.email} a changé son mot de passe"
        )

        return redirect('/admins/dashboard/')

    return render(request, 'admins/admin_change_password.html', {
        'admin': admin
    })


@admin_session_required
def dashboard(request):
    admin_id = request.session.get('admin_id')
    admin_email = request.session.get('admin_email')
    role = request.session.get('admin_role')

    total_members = Member.objects.count()
    total_admins = AdminUser.objects.count()

    today = timezone.localdate()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    global_today = Member.objects.filter(created_at__date=today).count()
    global_this_week = Member.objects.filter(created_at__date__gte=start_of_week).count()
    global_this_month = Member.objects.filter(created_at__date__gte=start_of_month).count()
    global_this_year = Member.objects.filter(created_at__date__gte=start_of_year).count()

    admin_today = Member.objects.filter(created_by_id=admin_id, created_at__date=today).count()
    admin_this_week = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_week).count()
    admin_this_month = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_month).count()
    admin_this_year = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_year).count()

    return render(request, 'admins/dashboard.html', {
        'email': admin_email,
        'role': role,
        'total_members': total_members,
        'total_admins': total_admins,
        'global_today': global_today,
        'global_this_week': global_this_week,
        'global_this_month': global_this_month,
        'global_this_year': global_this_year,
        'admin_today': admin_today,
        'admin_this_week': admin_this_week,
        'admin_this_month': admin_this_month,
        'admin_this_year': admin_this_year,
    })


@admin_session_required
def members_hub(request):
    return render(request, 'admins/members_hub.html')


@admin_session_required
def admins_hub(request):
    return render(request, 'admins/admins_hub.html')


@admin_session_required
def create_info_post(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        content = (request.POST.get('content') or '').strip()
        video_url = (request.POST.get('video_url') or '').strip() or None
        image = request.FILES.get('image')

        if not title or not content:
            return HttpResponse("Titre et contenu obligatoires ❌")

        admin = AdminUser.objects.get(id=request.session.get('admin_id'))

        InfoPost.objects.create(
            title=title,
            content=content,
            video_url=video_url,
            image=image,
            is_published=True,
            published_at=timezone.now(),
            created_by=admin
        )

        return redirect('/admins/info-posts/')

    return render(request, 'admins/create_info_post.html')


@admin_session_required
def info_post_list(request):
    posts = InfoPost.objects.all().order_by('-created_at')

    return render(request, 'admins/info_post_list.html', {
        'posts': posts
    })



@admin_session_required
def edit_info_post(request, post_id):
    try:
        post = InfoPost.objects.get(id=post_id)
    except InfoPost.DoesNotExist:
        return HttpResponse("Post introuvable ❌")

    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        content = (request.POST.get('content') or '').strip()
        video_url = (request.POST.get('video_url') or '').strip() or None
        image = request.FILES.get('image')

        if not title or not content:
            return HttpResponse("Titre et contenu obligatoires ❌")

        post.title = title
        post.content = content
        post.video_url = video_url

        if image:
            post.image = image

        if not post.published_at:
            post.published_at = timezone.now()

        post.save()

        return redirect('/admins/info-posts/')

    return render(request, 'admins/edit_info_post.html', {
        'post': post
    })


@admin_session_required
def delete_info_post(request, post_id):
    if request.method != 'POST':
        return redirect('/admins/info-posts/')

    try:
        post = InfoPost.objects.get(id=post_id)
    except InfoPost.DoesNotExist:
        return HttpResponse("Post introuvable ❌")

    post.delete()
    return redirect('/admins/info-posts/')    


def member_info_posts(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    posts = InfoPost.objects.filter(is_published=True).order_by('-published_at', '-created_at')

    return render(request, 'admins/member_info_posts.html', {
        'member': member,
        'posts': posts
    })



@super_admin_required
def admin_list(request):
    search_nim = (request.GET.get('nim') or '').strip()

    admins = AdminUser.objects.all().order_by('-created_at')

    if search_nim:
        admins = admins.filter(nim__icontains=search_nim)

    return render(request, 'admins/admins_list.html', {
        'admins': admins,
        'search_nim': search_nim,
    })


@super_admin_required
def create_admin(request):
    if request.method == 'POST':
        nim = (request.POST.get('nim') or '').strip()
        email = (request.POST.get('email') or '').strip().lower()
        role = (request.POST.get('role') or '').strip()

        if not nim:
            return HttpResponse("Le NIM est obligatoire ❌")

        if role not in ['super_admin', 'admin']:
            return HttpResponse("Rôle invalide ❌")

        try:
            member = Member.objects.get(nim=nim)
        except Member.DoesNotExist:
            return HttpResponse("Aucun membre trouvé avec ce NIM ❌")

        if AdminUser.objects.filter(nim=nim).exists():
            return HttpResponse("Un administrateur existe déjà avec ce NIM ❌")

        if AdminUser.objects.filter(email=email).exists():
            return HttpResponse("Cet email existe déjà ❌")

        if role == 'super_admin' and request.session.get('admin_email') != 'admin@fondaction.com':
            return HttpResponse("Seul le super admin principal peut créer un super admin ❌")

        temporary_password = generate_temporary_password()

        new_admin = AdminUser.objects.create(
            first_name=member.first_name,
            last_name=member.last_name,
            phone=member.phone,
            nim=member.nim,
            email=email,
            password=make_password(temporary_password),
            role=role,
            status=ADMIN_STATUS_ACTIVE,
            must_change_password=True
        )

        current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

        log_activity(
            admin_user=current_admin,
            action='create_admin',
            target_type='admin',
            target_id=new_admin.id,
            details=f"{current_admin.email} a créé l’admin {new_admin.email} lié au NIM {new_admin.nim}"
        )

        return HttpResponse(
            f"Administrateur créé avec succès ✅<br>"
            f"Mot de passe provisoire : <strong>{temporary_password}</strong><br>"
            f"L’administrateur devra changer ce mot de passe à sa première connexion."
        )

    return render(request, 'admins/create_admin.html')


def get_admin_members_with_payment_status(admin, start_date='', end_date='', payment_status='all'):
    members = Member.objects.filter(created_by=admin).order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    paid_transactions = MemberTransaction.objects.filter(
        member=OuterRef('pk'),
        transaction_type='payment',
        status='success'
    )

    members = members.annotate(
        has_paid=Exists(paid_transactions)
    )

    if payment_status == 'paid':
        members = members.filter(has_paid=True)
    elif payment_status == 'unpaid':
        members = members.filter(has_paid=False)

    return members


def get_global_members_with_payment_status(start_date='', end_date='', payment_status='all'):
    members = Member.objects.select_related('created_by').order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    paid_transactions = MemberTransaction.objects.filter(
        member=OuterRef('pk'),
        transaction_type='payment',
        status='success'
    )

    members = members.annotate(
        has_paid=Exists(paid_transactions),
        total_paid_amount=Sum(
            'transactions__amount',
            filter=Q(
                transactions__transaction_type='payment',
                transactions__status='success'
            )
        )
    )

    if payment_status == 'paid':
        members = members.filter(has_paid=True)
    elif payment_status == 'unpaid':
        members = members.filter(has_paid=False)

    return members


@admin_session_required
def admin_detail(request, admin_id):
    if request.session.get('admin_role') != 'super_admin':
        return HttpResponse("Accès refusé ❌")

    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    total_created_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='all',
    ).count()

    total_paid_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='paid',
    ).count()

    total_unpaid_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='unpaid',
    ).count()

    return render(request, 'admins/admin_detail.html', {
        'admin_obj': admin,
        'members': members,
        'total_created_members': total_created_members,
        'total_paid_members': total_paid_members,
        'total_unpaid_members': total_unpaid_members,
        'start_date': start_date,
        'end_date': end_date,
        'payment_status': payment_status,
    })


@super_admin_required
def global_admin_performance(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    total_created_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='all',
    ).count()

    total_paid_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='paid',
    ).count()

    total_unpaid_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='unpaid',
    ).count()

    total_admins = AdminUser.objects.count()
    total_members_all_time = Member.objects.count()

    total_payments_amount = MemberTransaction.objects.filter(
        member__in=get_global_members_with_payment_status(
            start_date=start_date,
            end_date=end_date,
            payment_status='all',
        ),
        transaction_type='payment',
        status='success'
    ).aggregate(total=Sum('amount'))['total'] or 0

    

    # Version plus robuste pour le résumé par admin
    admins_summary_data = []
    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        admin_members = Member.objects.filter(created_by=admin)

        if start_date:
            admin_members = admin_members.filter(created_at__date__gte=start_date)

        if end_date:
            admin_members = admin_members.filter(created_at__date__lte=end_date)

        created_count = admin_members.count()

        paid_count = admin_members.filter(
            transactions__transaction_type='payment',
            transactions__status='success'
        ).distinct().count()

        unpaid_count = created_count - paid_count

        admins_summary_data.append({
            'admin': admin,
            'created_count': created_count,
            'paid_count': paid_count,
            'unpaid_count': unpaid_count,
        })

    admins_summary_data.sort(key=lambda x: x['created_count'], reverse=True)

    return render(request, 'admins/global_admin_performance.html', {
        'members': members,
        'total_created_members': total_created_members,
        'total_paid_members': total_paid_members,
        'total_unpaid_members': total_unpaid_members,
        'total_admins': total_admins,
        'total_members_all_time': total_members_all_time,
        'total_payments_amount': total_payments_amount,
        'admins_summary_data': admins_summary_data,
        'start_date': start_date,
        'end_date': end_date,
        'payment_status': payment_status,
    })


@super_admin_required
def export_global_admin_performance_excel(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Performance Globale"

    headers = [
        "Admin créateur",
        "Email admin",
        "Rôle admin",
        "Membre NIM",
        "Nom membre",
        "Prénom membre",
        "Téléphone membre",
        "Ville",
        "Date de création",
        "A payé ?",
        "Montant total payé",
    ]
    sheet.append(headers)

    for member in members:
        admin = member.created_by

        total_paid_amount = MemberTransaction.objects.filter(
            member=member,
            transaction_type='payment',
            status='success'
        ).aggregate(total=Sum('amount'))['total'] or 0

        sheet.append([
            f"{admin.last_name} {admin.first_name}" if admin else "",
            admin.email if admin else "",
            admin.role if admin else "",
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            "Oui" if member.has_paid else "Non",
            float(total_paid_amount),
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename=performance_globale_{payment_status}.xlsx'
    )

    workbook.save(response)
    return response


@super_admin_required
def export_admins_summary_excel(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Résumé Admins"

    headers = [
        "NIM Admin",
        "Nom",
        "Prénom",
        "Email",
        "Rôle",
        "Membres créés",
        "Ont payé",
        "N’ont pas payé",
    ]
    sheet.append(headers)

    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        admin_members = Member.objects.filter(created_by=admin)

        if start_date:
            admin_members = admin_members.filter(created_at__date__gte=start_date)

        if end_date:
            admin_members = admin_members.filter(created_at__date__lte=end_date)

        created_count = admin_members.count()

        paid_count = admin_members.filter(
            transactions__transaction_type='payment',
            transactions__status='success'
        ).distinct().count()

        unpaid_count = created_count - paid_count

        sheet.append([
            admin.nim,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.role,
            created_count,
            paid_count,
            unpaid_count,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=resume_admins.xlsx'

    workbook.save(response)
    return response


@super_admin_required
def reset_admin_password(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    if admin.role == 'super_admin' and request.session.get('admin_email') != 'admin@fondaction.com':
        return HttpResponse("Seul le super admin principal peut réinitialiser le mot de passe d’un super admin ❌")

    temporary_password = generate_temporary_password()
    admin.password = make_password(temporary_password)
    admin.must_change_password = True
    admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reset_admin_password',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a réinitialisé le mot de passe de {admin.email}"
    )

    return HttpResponse(
        f"Mot de passe réinitialisé avec succès ✅<br>"
        f"Nouveau mot de passe provisoire : <strong>{temporary_password}</strong><br>"
        f"L’administrateur devra le changer à sa prochaine connexion."
    )


@super_admin_required
def suspend_admin(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    if admin.id == request.session.get('admin_id'):
        return HttpResponse("Tu ne peux pas te suspendre toi-même ❌")

    if admin.role == 'super_admin':
        return HttpResponse("Impossible de suspendre un super admin ❌")

    admin.status = ADMIN_STATUS_SUSPENDED
    admin.save(update_fields=['status', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='suspend_admin',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a suspendu {admin.email}"
    )

    return redirect('/admins/list/')


@super_admin_required
def reactivate_admin(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    admin.status = ADMIN_STATUS_ACTIVE
    admin.save(update_fields=['status', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reactivate_admin',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a réactivé {admin.email}"
    )

    return redirect('/admins/list/')


@super_admin_required
def activity_logs(request):
    from logs.models import ActivityLog

    logs = ActivityLog.objects.all().order_by('-created_at')
    return render(request, 'admins/activity_logs.html', {
        'logs': logs
    })


@admin_session_required
def create_member(request):
    if request.method == 'POST':
        try:
            current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
        except AdminUser.DoesNotExist:
            request.session.flush()
            return redirect('/admins/login/')

        try:
            validate_uploaded_image(request.FILES.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('signature'), ['.png'], max_size_mb=2)

            member = create_member_record(request.POST, request.FILES, current_admin)
        except ValueError as e:
            return HttpResponse(f"{str(e)} ❌")
        except Exception:
            return HttpResponse("Erreur serveur ❌")

        log_activity(
            admin_user=current_admin,
            action='create_member',
            target_type='member',
            target_id=member.id,
            details=f"{current_admin.email} a créé le membre {member.nim}"
        )

        return redirect('/admins/members/')

    return render(request, 'admins/create_member.html')


@admin_session_required
def member_list(request):
    try:
        current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    nim = (request.GET.get('nim') or '').strip()
    phone = (request.GET.get('phone') or '').strip()

    members = Member.objects.all().order_by('-created_at')

    if nim:
        members = members.filter(nim__icontains=nim)

    if phone:
        members = members.filter(phone__icontains=phone)

    return render(request, 'admins/member_list.html', {
        'members': members,
        'admin': current_admin,
        'nim': nim,
        'phone': phone,
    })

@admin_session_required
def member_detail(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    transactions = MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')

    return render(request, 'admins/member_detail.html', {
        'member': member,
        'transactions': transactions,
    })


def member_login(request):
    if request.method == 'POST':
        nim = (request.POST.get('nim') or '').strip()
        pin = (request.POST.get('pin') or '').strip()

        try:
            member = Member.objects.get(nim=nim)

            if member.status == MEMBER_STATUS_SUSPENDED:
                return HttpResponse("Compte suspendu ❌")

            if member.status != MEMBER_STATUS_ACTIVE:
                return HttpResponse("Compte membre inactif ❌")

            if member.is_locked:
                return HttpResponse("Compte bloqué ❌ Veuillez contacter l’administration pour une réinitialisation.")

            if check_password(pin, member.member_pin):
                member.failed_pin_attempts = 0
                member.save(update_fields=['failed_pin_attempts'])

                request.session['member_id'] = member.id
                request.session['member_nim'] = member.nim
                request.session['member_name'] = f"{member.first_name} {member.last_name}"

                if member.must_change_pin:
                    return redirect('/admins/member-change-pin/')

                return redirect('/admins/member-space/')

            member.failed_pin_attempts += 1

            if member.failed_pin_attempts >= MAX_MEMBER_PIN_ATTEMPTS:
                member.is_locked = True
                member.save(update_fields=['failed_pin_attempts', 'is_locked'])
                return HttpResponse(
                    "Compte bloqué ❌ Vous avez dépassé 3 tentatives incorrectes. "
                    "Veuillez contacter l’administration pour une réinitialisation."
                )

            member.save(update_fields=['failed_pin_attempts'])
            remaining = MAX_MEMBER_PIN_ATTEMPTS - member.failed_pin_attempts
            return HttpResponse(f"PIN incorrect ❌ Il vous reste {remaining} tentative(s).")

        except Member.DoesNotExist:
            return HttpResponse("Membre introuvable ❌")

    return render(request, 'admins/member_login.html')


@member_session_required
def member_change_pin(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    if request.method == 'POST':
        new_pin = request.POST.get('new_pin')
        confirm_pin = request.POST.get('confirm_pin')

        if not new_pin or not new_pin.isdigit() or len(new_pin) != 5:
            return HttpResponse("Le nouveau PIN doit contenir exactement 5 chiffres ❌")

        if new_pin != confirm_pin:
            return HttpResponse("Les deux PIN ne correspondent pas ❌")

        member.member_pin = make_password(new_pin)
        member.must_change_pin = False
        member.failed_pin_attempts = 0
        member.is_locked = False
        member.save(update_fields=['member_pin', 'must_change_pin', 'failed_pin_attempts', 'is_locked'])

        return redirect('/admins/member-space/')

    return render(request, 'admins/member_change_pin.html')

@member_session_required
def member_space(request):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    total_contributions = get_total_contributions(member)
    available_balance = get_available_balance(member)
    recent_transactions = get_recent_transactions(member)

    return render(request, 'admins/member_space.html', {
        'member': member,
        'total_contributions': total_contributions,
        'available_balance': available_balance,
        'recent_transactions': recent_transactions,
    })

@member_session_required
def member_withdrawal(request):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    error_message = None
    success_message = None

    if request.method == 'POST':
        amount = (request.POST.get('amount') or '').strip()
        receiver_phone = (request.POST.get('receiver_phone') or '').strip()
        reason = (request.POST.get('reason') or '').strip()
        pin = (request.POST.get('pin') or '').strip()

        try:
            create_withdrawal_request(
                member=member,
                amount=amount,
                receiver_phone=receiver_phone,
                reason=reason,
                pin=pin,
            )
            success_message = "Votre demande de retrait a été envoyée avec succès. Elle est en attente de validation."
        except ValueError as e:
            error_message = str(e)
        except Exception:
            error_message = "Une erreur est survenue lors de la demande de retrait."

    available_balance = get_available_balance(member)

    return render(request, 'admins/member_withdrawal.html', {
        'member': member,
        'available_balance': available_balance,
        'error_message': error_message,
        'success_message': success_message,
    })

@admin_session_required
def withdrawal_requests(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    requests_list = WithdrawalRequest.objects.select_related(
        'member',
        'transaction',
        'processed_by',
    ).order_by('-created_at')

    return render(request, 'admins/withdrawal_requests.html', {
        'requests_list': requests_list,
    })


@admin_session_required
def approve_withdrawal(request, withdrawal_id):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    if request.method != 'POST':
        return redirect('/admins/withdrawal-requests/')

    try:
        admin_user = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    withdrawal_request = get_object_or_404(WithdrawalRequest, id=withdrawal_id)

    admin_note = (request.POST.get('admin_note') or '').strip()

    try:
        approve_withdrawal_request(
            withdrawal_request=withdrawal_request,
            admin_user=admin_user,
            admin_note=admin_note,
        )
    except ValueError as e:
        return HttpResponse(str(e))
    except Exception:
        return HttpResponse("Erreur lors de la validation du retrait.")

    return redirect('/admins/withdrawal-requests/')


@admin_session_required
def reject_withdrawal(request, withdrawal_id):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    if request.method != 'POST':
        return redirect('/admins/withdrawal-requests/')

    try:
        admin_user = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    withdrawal_request = get_object_or_404(WithdrawalRequest, id=withdrawal_id)

    admin_note = (request.POST.get('admin_note') or '').strip()

    try:
        reject_withdrawal_request(
            withdrawal_request=withdrawal_request,
            admin_user=admin_user,
            admin_note=admin_note,
        )
    except ValueError as e:
        return HttpResponse(str(e))
    except Exception:
        return HttpResponse("Erreur lors du refus du retrait.")

    return redirect('/admins/withdrawal-requests/')





@member_session_required
def member_logout(request):
    request.session.pop('member_id', None)
    request.session.pop('member_nim', None)
    request.session.pop('member_name', None)
    return redirect('/admins/member-login/')


@super_admin_required
def reset_member_pin(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    temporary_pin = generate_temporary_pin()
    member.member_pin = make_password(temporary_pin)
    member.must_change_pin = True
    member.failed_pin_attempts = 0
    member.is_locked = False
    member.save(update_fields=['member_pin', 'must_change_pin', 'failed_pin_attempts', 'is_locked'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reset_member_pin',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a réinitialisé le PIN du membre {member.nim}"
    )

    return HttpResponse(
        f"PIN réinitialisé avec succès ✅<br>"
        f"Nouveau PIN provisoire : <strong>{temporary_pin}</strong><br>"
        f"Le membre devra le changer à la prochaine connexion."
    )


@member_session_required
def member_card(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_card.html', {
        'member': member
    })


@member_session_required
def download_member_card_pdf(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    template = get_template('admins/member_card_pdf.html')
    html = template.render({
        'member': member,
        'photo_url': request.build_absolute_uri(member.photo.url) if member.photo else '',
        'signature_url': request.build_absolute_uri(member.signature.url) if member.signature else '',
        'logo_url': request.build_absolute_uri('/static/logo-fondaction.png'),
        'card_bg_url': request.build_absolute_uri('/static/card-bg.png'),
        'card_back_bg_url': request.build_absolute_uri('/static/card-back-bg.png'),
    })

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if pdf.err:
        return HttpResponse("Erreur lors de la génération du PDF ❌")

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="carte_{member.nim}.pdf"'
    return response

@admin_session_required
def edit_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    if request.method == 'POST':
        member.first_name = (request.POST.get('first_name') or '').strip()
        member.last_name = (request.POST.get('last_name') or '').strip()
        member.birth_date = request.POST.get('birth_date')
        member.birth_place = (request.POST.get('birth_place') or '').strip()
        member.department = (request.POST.get('department') or '').strip()
        member.commune = (request.POST.get('commune') or '').strip()
        member.city = (request.POST.get('city') or '').strip()
        member.district = (request.POST.get('district') or '').strip()
        member.phone = (request.POST.get('phone') or '').strip() or None
        member.id_card_type = (request.POST.get('id_card_type') or '').strip()
        member.id_card_number = (request.POST.get('id_card_number') or '').strip()
        member.emergency_last_name = (request.POST.get('emergency_last_name') or '').strip() or None
        member.emergency_first_name = (request.POST.get('emergency_first_name') or '').strip() or None
        member.emergency_phone = (request.POST.get('emergency_phone') or '').strip() or None

        if not member.id_card_number:
            return HttpResponse("Le numéro de pièce est obligatoire ❌")

        if Member.objects.filter(id_card_number=member.id_card_number).exclude(id=member.id).exists():
            return HttpResponse("Un autre membre utilise déjà ce numéro de pièce ❌")

        if member.phone and Member.objects.filter(phone=member.phone).exclude(id=member.id).exists():
            return HttpResponse("Un autre membre utilise déjà ce numéro de téléphone ❌")

        try:
            validate_uploaded_image(request.FILES.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('signature'), ['.png'], max_size_mb=2)
        except ValueError as e:
            return HttpResponse(f"{str(e)} ❌")

        if request.FILES.get('photo'):
            member.photo = request.FILES.get('photo')

        if request.FILES.get('id_card_front'):
            member.id_card_front = request.FILES.get('id_card_front')

        if request.FILES.get('id_card_back'):
            member.id_card_back = request.FILES.get('id_card_back')

        if request.FILES.get('signature'):
            member.signature = request.FILES.get('signature')

        member.save()

        try:
            current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
        except AdminUser.DoesNotExist:
            request.session.flush()
            return redirect('/admins/login/')

        log_activity(
            admin_user=current_admin,
            action='edit_member',
            target_type='member',
            target_id=member.id,
            details=f"{current_admin.email} a modifié le membre {member.nim}"
        )

        return redirect(f'/admins/members/{member.id}/')

    return render(request, 'admins/edit_member.html', {
        'member': member
    })


@admin_session_required
def suspend_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    member.status = MEMBER_STATUS_SUSPENDED
    member.save(update_fields=['status'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='suspend_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a suspendu le membre {member.nim}"
    )

    return redirect(f'/admins/members/{member.id}/')


@admin_session_required
def activate_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    member.status = MEMBER_STATUS_ACTIVE
    member.save(update_fields=['status'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='activate_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a réactivé le membre {member.nim}"
    )

    return redirect(f'/admins/members/{member.id}/')


@admin_session_required
def member_creation_history(request):
    admin_id = request.session.get('admin_id')
    role = request.session.get('admin_role')

    if role == 'super_admin':
        members = Member.objects.all().order_by('-created_at')
    else:
        members = Member.objects.filter(created_by_id=admin_id).order_by('-created_at')

    return render(request, 'admins/member_creation_history.html', {
        'members': members,
        'role': role,
    })


@super_admin_required
def admin_performance_detail(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    members = Member.objects.filter(created_by=admin).order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    total_members = members.count()

    return render(request, 'admins/admin_performance_detail.html', {
        'admin_obj': admin,
        'members': members,
        'total_members': total_members,
        'start_date': start_date,
        'end_date': end_date,
    })


@super_admin_required
def export_admin_performance_excel(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Performance Admin"

    headers = [
        "Admin NIM",
        "Admin Nom",
        "Admin Prénom",
        "Admin Email",
        "Rôle",
        "Membre NIM",
        "Membre Nom",
        "Membre Prénom",
        "Téléphone membre",
        "Ville",
        "Date de création",
        "A payé ?",
    ]
    sheet.append(headers)

    for member in members:
        sheet.append([
            admin.nim,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.role,
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            "Oui" if member.has_paid else "Non",
        ])

    filename_suffix = payment_status
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename=performance_admin_{admin.id}_{filename_suffix}.xlsx'
    )

    workbook.save(response)
    return response


@admin_session_required
def export_members_excel(request):
    role = request.session.get('admin_role')
    admin_id = request.session.get('admin_id')

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Membres"

    headers = [
        "NIM",
        "Nom",
        "Prénom",
        "Téléphone",
        "Ville",
        "Date de création",
        "Créé par"
    ]
    sheet.append(headers)

    members = Member.objects.all().order_by('-created_at')
    if role != 'super_admin':
        members = members.filter(created_by_id=admin_id)

    for member in members:
        sheet.append([
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            member.created_by.email if member.created_by else ""
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=liste_membres.xlsx'

    workbook.save(response)
    return response


@super_admin_required
def export_admins_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Admins"

    headers = [
        "ID",
        "Nom",
        "Prénom",
        "Email",
        "Téléphone",
        "Rôle",
        "Statut",
        "Date de création"
    ]
    sheet.append(headers)

    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        sheet.append([
            admin.id,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.phone,
            admin.role,
            admin.status,
            admin.created_at.strftime("%d/%m/%Y %H:%M") if admin.created_at else ""
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=liste_admins.xlsx'

    workbook.save(response)
    return response


@member_session_required
def member_payment(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    now = timezone.localtime()
    french_months = {
        1: "Janvier",
        2: "Février",
        3: "Mars",
        4: "Avril",
        5: "Mai",
        6: "Juin",
        7: "Juillet",
        8: "Août",
        9: "Septembre",
        10: "Octobre",
        11: "Novembre",
        12: "Décembre",
    }

    current_month_label = f"{french_months[now.month]} {now.year}"

    return render(request, 'admins/payment_page.html', {
        'member': member,
        'current_month_label': current_month_label,
        'amount': DEFAULT_MONTHLY_CONTRIBUTION,
    })


@member_session_required
def start_member_payment_view(request):
    if request.method != 'POST':
        return redirect('/admins/member-payment/')

    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    try:
        payment_url, _attempt = start_fedapay_payment(
            member=member,
            amount=DEFAULT_MONTHLY_CONTRIBUTION,
            months=DEFAULT_PAYMENT_MONTHS,
            callback_url=request.build_absolute_uri('/admins/payment-return/'),
        )
        return redirect(payment_url)
    except Exception as e:
        return HttpResponse(f"Erreur paiement : {str(e)} ❌")


def start_member_payment(request):
    return start_member_payment_view(request)


@member_session_required
def payment_return(request):
    status = request.GET.get('status', '')
    transaction_id = request.GET.get('id', '')

    return render(request, 'admins/payment_return.html', {
        'status': status,
        'transaction_id': transaction_id,
    })


@member_session_required
def member_transactions(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    transactions = MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')

    return render(request, 'admins/member_transactions.html', {
        'member': member,
        'transactions': transactions
    }) 

@member_session_required
def member_transaction_detail(request, transaction_id):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    transaction = get_object_or_404(
        MemberTransaction,
        id=transaction_id,
        member=member
    )

    withdrawal_request = None
    try:
        withdrawal_request = transaction.withdrawal_request
    except WithdrawalRequest.DoesNotExist:
        withdrawal_request = None
    except AttributeError:
        withdrawal_request = None

    return render(request, 'admins/member_transaction_detail.html', {
        'member': member,
        'transaction': transaction,
        'withdrawal_request': withdrawal_request,
    })   

@member_session_required
def member_profile(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_profile.html', {
        'member': member
    })

@member_session_required
def member_settings(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_settings.html', {
        'member': member
    })



@admin_session_required
def search_transactions(request):
    admin_id = request.session.get('admin_id')

    if not admin_id:
        return redirect('/admins/login/')

    query = (request.GET.get('q') or '').strip()
    transactions = []

    if query:
        transactions = MemberTransaction.objects.select_related('member').filter(
            receipt_number__icontains=query
        ).order_by('-created_at')

    return render(request, 'admins/search_transactions.html', {
        'query': query,
        'transactions': transactions,
    })

def member_assistance(request):
    return render(request, 'admins/member_assistance.html')


def visitor_home(request):
    return render(request, 'admins/visitor_home.html')

def secure_registration_page(request):
    return render(request, 'admins/secure_registration.html')

def about_page(request):
    return render(request, 'admins/about.html')

def privacy_policy_page(request):
    return render(request, 'admins/privacy_policy.html')


def terms_services_page(request):
    return render(request, 'admins/terms_services.html')

def contact_page(request):
    return render(request, 'admins/contact.html')


def root_router(request):
    host = request.get_host().split(':')[0]

    if host == "admin.fondactionsarl.com":
        return redirect('/admins/login/')

    if host == "api.fondactionsarl.com":
        return JsonResponse({
            "success": True,
            "message": "FondAction API is running"
        })

    return redirect('/admins/visiteur/')

def robots_txt(request):
    host = request.get_host()

    if host.startswith("admin.") or host.startswith("api."):
        return HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")

    return HttpResponse("User-agent: *\nAllow: /", content_type="text/plain")



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()

    return request.META.get('REMOTE_ADDR', '')


def is_rate_limited(request, key_prefix, max_attempts=5, window_seconds=600):
    ip = get_client_ip(request)
    cache_key = f"{key_prefix}:{ip}"

    attempts = cache.get(cache_key, 0)

    if attempts >= max_attempts:
        return True

    cache.set(cache_key, attempts + 1, timeout=window_seconds)
    return False


def sitemap_xml(request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://fondactionsarl.com/</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/about/</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/contact/</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/privacy-policy/</loc>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/terms-services/</loc>
        <priority>0.5</priority>
    </url>
</urlset>
"""
    return HttpResponse(xml, content_type="application/xml")



import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("DJANGO_SECRET_KEY manquant dans le .env")

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "sqlite")
if not DEBUG and DATABASE_ENGINE == "sqlite":
    print("ATTENTION: le projet tourne en production avec SQLite")

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'admins',
    'members',
    'logs',
    'cloudinary',
    'cloudinary_storage',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

if DATABASE_ENGINE == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', ''),
            'USER': os.getenv('POSTGRES_USER', ''),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
            'CONN_MAX_AGE': 60,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Porto-Novo'
USE_I18N = True
USE_TZ = True

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("DJANGO_CORS_ALLOWED_ORIGINS", "").split(",")
    if origin.strip()
]
CORS_ALLOW_CREDENTIALS = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STORAGES = {
    'default': {
        'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

FEDAPAY_MODE = os.getenv("FEDAPAY_MODE", "sandbox")
FEDAPAY_PUBLIC_KEY = os.getenv("FEDAPAY_PUBLIC_KEY", "")
FEDAPAY_SECRET_KEY = os.getenv("FEDAPAY_SECRET_KEY", "")
FEDAPAY_WEBHOOK_SECRET = os.getenv("FEDAPAY_WEBHOOK_SECRET", "")

if FEDAPAY_MODE == "sandbox":
    FEDAPAY_API_BASE = "https://sandbox-api.fedapay.com/v1"
else:
    FEDAPAY_API_BASE = "https://api.fedapay.com/v1"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sécurité production
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = False
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = os.getenv("DJANGO_SECURE_SSL_REDIRECT", "True") == "True"
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Sessions
SESSION_COOKIE_AGE = 60 * 60 * 2  # 2 heures
SESSION_SAVE_EVERY_REQUEST = True
LOGIN_RATE_LIMIT_MAX_ATTEMPTS = 5
LOGIN_RATE_LIMIT_WINDOW_SECONDS = 10 * 60  # 10 minutes

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'




from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from admins.web_views import root_router
from admins.web_views import sitemap_xml

urlpatterns = [
    path('', root_router, name='root_router'),
    path('admins/', include('admins.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.db import models
from admins.models import AdminUser


class ActivityLog(models.Model):
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    target_type = models.CharField(max_length=50, null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='success')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_user.email} - {self.action}"



from decimal import Decimal

DEFAULT_MONTHLY_CONTRIBUTION = Decimal("1200.00")
DEFAULT_PAYMENT_MONTHS = 1

MEMBER_STATUS_ACTIVE = "active"
MEMBER_STATUS_SUSPENDED = "suspended"
MEMBER_STATUS_INACTIVE = "inactive"

ADMIN_STATUS_ACTIVE = "active"
ADMIN_STATUS_SUSPENDED = "suspended"
ADMIN_STATUS_INACTIVE = "inactive"

ADMIN_ROLE_SUPER = "super_admin"
ADMIN_ROLE_STANDARD = "admin"

MAX_MEMBER_PIN_ATTEMPTS = 3
TEMP_ADMIN_PASSWORD_LENGTH = 12
TEMP_MEMBER_PIN_LENGTH = 5




from django.db import models
from admins.models import AdminUser


class Member(models.Model):
    CARD_TYPE_CHOICES = [
        ('CIP', 'CIP'),
        ('NPI', 'NPI'),
        ('CEDEAO', 'CEDEAO'),
        ('PASSEPORT', 'PASSEPORT'),
    ]

    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('inactive', 'Inactif'),
        ('suspended', 'Suspendu'),
    ]

    nim = models.CharField(max_length=20, unique=True, null=True, blank=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True, db_index=True)

    photo = models.ImageField(upload_to='members/photos/', null=True, blank=True)

    id_card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
    id_card_number = models.CharField(max_length=100, unique=True, db_index=True)
    id_card_front = models.ImageField(upload_to='members/id_cards/front/', null=True, blank=True)
    id_card_back = models.ImageField(upload_to='members/id_cards/back/', null=True, blank=True)

    signature = models.ImageField(upload_to='members/signatures/', null=True, blank=True)
    member_pin = models.CharField(max_length=255, null=True, blank=True)

    emergency_last_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_first_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_phone = models.CharField(max_length=20, null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    must_change_pin = models.BooleanField(default=False)
    failed_pin_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)

    created_by = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nim} - {self.first_name} {self.last_name}"


class MemberTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('payment', 'Paiement'),
        ('withdrawal', 'Retrait'),
    ]

    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('success', 'Succès'),
        ('failed', 'Échoué'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    receipt_number = models.CharField(max_length=30, unique=True, null=True, blank=True, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    validated_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=['member', 'transaction_type', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.reference} - {self.member.nim} - {self.transaction_type}"


class WithdrawalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='withdrawal_requests'
    )
    transaction = models.OneToOneField(
        MemberTransaction,
        on_delete=models.CASCADE,
        related_name='withdrawal_request'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    receiver_phone = models.CharField(max_length=20)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, null=True)
    processed_by = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='processed_withdrawals'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['member', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Retrait {self.member.nim} - {self.amount} - {self.status}"


class InfoPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='members/info_posts/images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='info_posts'
    )

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title


class FedapayPaymentAttempt(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('failed', 'Failed'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='fedapay_attempts'
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    transaction_reference = models.CharField(max_length=150, blank=True, null=True)
    nim = models.CharField(max_length=50)
    months = models.PositiveIntegerField(default=1)
    monthly_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_url = models.TextField(blank=True, null=True)
    fedapay_payload = models.JSONField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['member', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.nim} - {self.transaction_id} - {self.status}"



from decimal import Decimal

import requests
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from members.models import FedapayPaymentAttempt, MemberTransaction
from members.services import create_manual_payment_transaction


def build_fedapay_headers():
    return {
        "Authorization": f"Bearer {settings.FEDAPAY_SECRET_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def build_fedapay_verify_headers():
    return {
        "Authorization": f"Bearer {settings.FEDAPAY_SECRET_KEY}",
        "Accept": "application/json",
    }


def start_fedapay_payment(member, amount, months, callback_url):
    amount = Decimal(str(amount))
    total_amount = amount * Decimal(str(months))

    payload = {
        "description": f"Cotisation mensuelle - {member.nim}",
        "amount": float(total_amount),
        "currency": {"iso": "XOF"},
        "callback_url": callback_url,
        "customer": {
            "firstname": member.first_name or "",
            "lastname": member.last_name or "",
            "email": f"{member.nim.lower()}@fondaction.local",
            "phone_number": {
                "number": member.phone or "00000000",
                "country": "bj",
            }
        }
    }

    create_response = requests.post(
        f"{settings.FEDAPAY_API_BASE}/transactions",
        headers=build_fedapay_headers(),
        json=payload,
        timeout=30,
    )
    create_data = create_response.json()

    if create_response.status_code not in [200, 201]:
        raise ValueError(f"Erreur FedaPay création : {create_data}")

    transaction_data = (
        create_data.get('v1/transaction')
        or create_data.get('transaction')
        or create_data
    )

    transaction_id = transaction_data.get('id')
    transaction_reference = transaction_data.get('reference')

    if not transaction_id:
        raise ValueError("Transaction FedaPay introuvable")

    attempt, _ = FedapayPaymentAttempt.objects.update_or_create(
        transaction_id=str(transaction_id),
        defaults={
            'member': member,
            'nim': member.nim,
            'months': months,
            'monthly_amount': amount,
            'total_amount': total_amount,
            'transaction_reference': transaction_reference,
            'status': 'pending',
            'fedapay_payload': create_data,
        }
    )

    token_response = requests.post(
        f"{settings.FEDAPAY_API_BASE}/transactions/{transaction_id}/token",
        headers=build_fedapay_headers(),
        json={"transaction_id": transaction_id},
        timeout=30,
    )
    token_data = token_response.json()

    if token_response.status_code not in [200, 201]:
        raise ValueError(f"Erreur FedaPay token : {token_data}")

    payment_url = (
        token_data.get('url')
        or token_data.get('token', {}).get('url')
        or token_data.get('v1/token', {}).get('url')
    )

    if not payment_url:
        raise ValueError("Lien de paiement introuvable")

    attempt.payment_url = payment_url
    attempt.save(update_fields=['payment_url', 'updated_at'])

    return payment_url, attempt


@transaction.atomic
def process_fedapay_webhook(payload):
    entity = payload.get('entity') or {}
    transaction_data = entity.get('data') or entity
    transaction_id = transaction_data.get('id')

    if not transaction_id:
        raise ValueError("Transaction introuvable")

    try:
        attempt = FedapayPaymentAttempt.objects.select_for_update().get(
            transaction_id=str(transaction_id)
        )
    except FedapayPaymentAttempt.DoesNotExist:
        raise ValueError("Tentative de paiement inexistante")

    try:
        verify_response = requests.get(
            f"{settings.FEDAPAY_API_BASE}/transactions/{transaction_id}",
            headers=build_fedapay_verify_headers(),
            timeout=30,
        )
    except requests.RequestException:
        raise ValueError("Erreur réseau lors de la vérification FedaPay")

    if verify_response.status_code not in [200, 201]:
        raise ValueError("Vérification FedaPay échouée")

    try:
        verify_data = verify_response.json()
    except Exception:
        raise ValueError("Réponse FedaPay invalide")

    transaction_verified = (
        verify_data.get('v1/transaction')
        or verify_data.get('transaction')
        or verify_data
    )

    verified_status = (transaction_verified.get('status') or '').lower()
    amount = Decimal(str(transaction_verified.get('amount', 0)))

    attempt.fedapay_payload = verify_data

    # 🔴 Paiement refusé
    if verified_status in ['declined', 'failed', 'canceled', 'cancelled']:
        attempt.status = 'declined'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'declined'

    # 🟡 En attente
    if verified_status not in ['approved', 'successful', 'success']:
        attempt.status = 'pending'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'pending'

    # 🔁 Anti double traitement
    if attempt.is_processed:
        return 'already_processed'

    # 🔒 Vérification montant
    if amount != attempt.total_amount:
        raise ValueError("Montant incohérent")

    # 🔒 Vérification membre
    if not attempt.member:
        raise ValueError("Membre invalide")

    existing = MemberTransaction.objects.filter(
        member=attempt.member,
        reference=str(transaction_id)
    ).first()

    if not existing:
        create_manual_payment_transaction(
            member=attempt.member,
            amount=amount,
            description=f'Paiement FedaPay ({attempt.months} mois)',
            reference=str(transaction_id),
            validated_at=timezone.now(),
        )

    attempt.status = 'approved'
    attempt.is_processed = True
    attempt.processed_at = timezone.now()
    attempt.save(
        update_fields=[
            'status',
            'is_processed',
            'processed_at',
            'fedapay_payload',
            'updated_at'
        ]
    )

    return 'approved'






from django.http import HttpResponse

from admins.models import AdminUser


def get_current_admin(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return None

    try:
        return AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return None


def admin_can_access_member(request, member):
    role = request.session.get('admin_role')
    admin_id = request.session.get('admin_id')

    if role == 'super_admin':
        return True

    return member.created_by_id == admin_id


def forbid_if_no_member_access(request, member):
    if not admin_can_access_member(request, member):
        return HttpResponse("Accès refusé à ce membre ❌")
    return None



from decimal import Decimal
import uuid

from PIL import Image
from django.contrib.auth.hashers import make_password, check_password
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from .models import Member, MemberTransaction, WithdrawalRequest


def generate_reference(prefix='TRX'):
    return f"{prefix}-{uuid.uuid4().hex[:10].upper()}"


def get_total_payments(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='payment',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_success_withdrawals(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_pending_withdrawals(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='pending'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_contributions(member):
    total_payments = get_total_payments(member)
    total_success_withdrawals = get_total_success_withdrawals(member)

    total = total_payments - total_success_withdrawals

    if total <= 0:
        return Decimal('0.00')

    return total


def get_available_balance(member):
    total_payments = get_total_payments(member)
    total_success_withdrawals = get_total_success_withdrawals(member)
    total_pending_withdrawals = get_total_pending_withdrawals(member)

    available = total_payments - total_success_withdrawals - total_pending_withdrawals

    if available <= 0:
        return Decimal('0.00')

    return available


def get_recent_transactions(member, limit=5):
    return MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')[:limit]


@transaction.atomic
def create_manual_payment_transaction(
    member,
    amount,
    description=None,
    reference=None,
    validated_at=None,
):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    months = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]

    now = timezone.now()
    current_month = f"{months[now.month - 1]} {now.year}"

    if not description:
        description = f"Paiement mensuel - {current_month}"

    if not reference:
        reference = generate_reference('PAY')

    if validated_at is None:
        validated_at = timezone.now()

    transaction_record, created = MemberTransaction.objects.get_or_create(
        reference=reference,
        defaults={
            'member': member,
            'transaction_type': 'payment',
            'amount': amount,
            'status': 'success',
            'description': description,
            'validated_at': validated_at,
        }
    )

    if not transaction_record.receipt_number:
        transaction_record.receipt_number = generate_receipt_number(transaction_record)
        transaction_record.save(update_fields=['receipt_number'])

    return transaction_record


def generate_receipt_number(transaction):
    return f"RCPT-FAS-{transaction.created_at.year}-{transaction.id:08d}"    


@transaction.atomic
def create_withdrawal_request(member, amount, receiver_phone, reason, pin):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    if not receiver_phone:
        raise ValueError("Le numéro destinataire est obligatoire.")

    if not pin:
        raise ValueError("Le code PIN est obligatoire.")

    member = Member.objects.select_for_update().get(pk=member.pk)

    if not member.member_pin or not check_password(pin, member.member_pin):
        raise ValueError("Code PIN incorrect.")

    available_balance = get_available_balance(member)
    if amount > available_balance:
        raise ValueError("Solde insuffisant pour effectuer ce retrait.")

    transaction_record = MemberTransaction.objects.create(
        member=member,
        transaction_type='withdrawal',
        amount=amount,
        reference=generate_reference('WDR'),
        status='pending',
        description='Retrait',
    )

    transaction_record.receipt_number = generate_receipt_number(transaction_record)
    transaction_record.save(update_fields=['receipt_number'])

    withdrawal_request = WithdrawalRequest.objects.create(
        member=member,
        transaction=transaction_record,
        amount=amount,
        receiver_phone=receiver_phone,
        reason=reason or '',
        status='pending',
    )

    return withdrawal_request


@transaction.atomic
def approve_withdrawal_request(withdrawal_request, admin_user, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    withdrawal_request.status = 'approved'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_by = admin_user
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.save(update_fields=[
        'status',
        'admin_note',
        'processed_by',
        'processed_at',
    ])

    transaction_record = withdrawal_request.transaction
    transaction_record.status = 'success'
    transaction_record.validated_at = timezone.now()
    transaction_record.save(update_fields=['status', 'validated_at'])

    return withdrawal_request


@transaction.atomic
def reject_withdrawal_request(withdrawal_request, admin_user, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    withdrawal_request.status = 'rejected'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_by = admin_user
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.save(update_fields=[
        'status',
        'admin_note',
        'processed_by',
        'processed_at',
    ])

    transaction_record = withdrawal_request.transaction
    transaction_record.status = 'failed'
    transaction_record.validated_at = timezone.now()
    transaction_record.save(update_fields=['status', 'validated_at'])

    return withdrawal_request


def validate_uploaded_image(uploaded_file, allowed_extensions=None, max_size_mb=20):
    if not uploaded_file:
        return

    allowed_extensions = allowed_extensions or ['.jpg', '.jpeg', '.png']

    filename = uploaded_file.name.lower()
    if not any(filename.endswith(ext) for ext in allowed_extensions):
        raise ValueError("Format de fichier non autorisé")

    if uploaded_file.size > max_size_mb * 1024 * 1024:
        raise ValueError(f"Le fichier dépasse {max_size_mb} Mo")

    try:
        uploaded_file.seek(0)
        img = Image.open(uploaded_file)
        img.verify()
        uploaded_file.seek(0)
    except Exception:
        raise ValueError("Fichier image invalide ou corrompu")


def create_member_record(data, files, current_admin):
    raw_pin = (data.get('member_pin') or '').strip()

    if not raw_pin or not raw_pin.isdigit() or len(raw_pin) != 5:
        raise ValueError("Le code PIN doit contenir exactement 5 chiffres")

    id_card_number = (data.get('id_card_number') or '').strip()
    phone = (data.get('phone') or '').strip() or None

    validate_uploaded_image(files.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('signature'), ['.png'], max_size_mb=2)

    if not id_card_number:
        raise ValueError("Le numéro de pièce est obligatoire")

    if Member.objects.filter(id_card_number=id_card_number).exists():
        raise ValueError("Un membre avec ce numéro de pièce existe déjà")

    if phone and Member.objects.filter(phone=phone).exists():
        raise ValueError("Un membre avec ce numéro de téléphone existe déjà")

    member = Member.objects.create(
        first_name=(data.get('first_name') or '').strip(),
        last_name=(data.get('last_name') or '').strip(),
        birth_date=data.get('birth_date'),
        birth_place=(data.get('birth_place') or '').strip(),
        department=(data.get('department') or '').strip(),
        commune=(data.get('commune') or '').strip(),
        city=(data.get('city') or '').strip(),
        district=(data.get('district') or '').strip(),
        phone=phone,
        photo=files.get('photo'),
        id_card_type=(data.get('id_card_type') or '').strip(),
        id_card_number=id_card_number,
        id_card_front=files.get('id_card_front'),
        id_card_back=files.get('id_card_back'),
        signature=files.get('signature'),
        member_pin=make_password(raw_pin),
        emergency_last_name=(data.get('emergency_last_name') or '').strip() or None,
        emergency_first_name=(data.get('emergency_first_name') or '').strip() or None,
        emergency_phone=(data.get('emergency_phone') or '').strip() or None,
        created_by=current_admin,
        status='active',
    )

    member.nim = f"FAS-{member.id:010d}"
    member.save(update_fields=['nim'])

    return member





# 🔐 Django
DJANGO_SECRET_KEY=o-g^l98!
DJANGO_DEBUG=False

DJANGO_ALLOWED_HOSTS=fondactionsarl.com,www.fondactionsarl.com,api.fondac>

DJANGO_CSRF_TRUSTED_ORIGINS=https://fondactionsarl.com,https://www.fondac>
DJANGO_CORS_ALLOWED_ORIGINS=https://fondactionsarl.com,https://www.fondac>

# 🐘 PostgreSQL
DATABASE_ENGINE=postgres
POSTGRES_DB=fondaction_db
POSTGRES_USER=fondaction_user
POSTGRES_PASSWORD=2000
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# 💳 FedaPay
FEDAPAY_MODE=sandbox
FEDAPAY_PUBLIC_KEY=pk_sandbox_jaHjXxytHbr850sAlKYuabvu
FEDAPAY_SECRET_KEY=sk_sandbox_EhhaVMxGTzD1LuGjXCuRPwjM
FEDAPAY_WEBHOOK_SECRET=wh_sandbox_xYRKqJqEXyRUsz6nSfROE1L0

CLOUDINARY_CLOUD_NAME=dmlcs5dkc
CLOUDINARY_API_KEY=817548348563658
CLOUDINARY_API_SECRET=a8YBODJJgnEBybusQjEveQQ71a8