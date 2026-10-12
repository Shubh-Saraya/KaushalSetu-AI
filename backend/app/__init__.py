* {
  box-sizing: border-box;
  font-family: Inter, 'Segoe UI', sans-serif;
}

body {
  margin: 0;
  background: #f4f7f9;
  color: #14213d;
}

button, input {
  font: inherit;
}

button {
  cursor: pointer;
}

.auth-shell {
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #0f172a, #0d9488);
  padding: 24px;
}

.auth-card {
  width: min(640px, 100%);
  background: white;
  border-radius: 22px;
  padding: 28px;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.18);
}

.brand-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.brand-mark {
  width: 54px;
  height: 54px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  background: linear-gradient(135deg, #0f172a, #0d9488);
  color: white;
  font-weight: 700;
}

.eyebrow {
  margin: 0;
  font-size: 12px;
  letter-spacing: 0.08em;
  color: #0d9488;
  text-transform: uppercase;
  font-weight: 700;
}

h1, h2, h3, h4, p {
  margin-top: 0;
}

.login-panel {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.login-panel label {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-weight: 600;
}

.login-panel input {
  border: 1px solid #dbe5eb;
  background: #f8fafc;
  padding: 12px 14px;
  border-radius: 10px;
  outline: none;
}

.login-panel button,
.secondary-button {
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg, #0f172a, #0d9488);
  color: white;
  padding: 12px 18px;
  font-weight: 700;
}

.demo-copy {
  margin-top: 8px;
  color: #475569;
  font-size: 0.92rem;
}

.app-shell {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 20px 48px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
  margin-bottom: 20px;
}

.stat-card,
.panel,
.candidate-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
}

.stat-card {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat-card span {
  color: #475569;
}

.stat-card strong {
  font-size: 1.6rem;
}

.content-grid,
.bottom-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

.panel {
  padding: 20px;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.pill {
  padding: 7px 10px;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 700;
}

.pill.warning {
  background: #fff7ed;
  color: #b45309;
}

.pill.success {
  background: #ecfdf5;
  color: #047857;
}

.pill.neutral {
  background: #eff6ff;
  color: #1d4ed8;
}

.candidate-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.candidate-card {
  padding: 18px;
}

.candidate-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
}

.candidate-head small {
  color: #0d9488;
  font-weight: 700;
}

.score-box {
  background: #ecfeff;
  border: 1px solid #a5f3fc;
  color: #0f172a;
  font-weight: 800;
  min-width: 52px;
  min-height: 52px;
  border-radius: 12px;
  display: grid;
  place-items: center;
}

.candidate-columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  margin-top: 12px;
}

.candidate-columns ul,
.bullet-list {
  margin: 8px 0 0;
  padding-left: 18px;
  color: #334155;
}

.meta-row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 14px;
  color: #475569;
  font-size: 0.85rem;
}

.meta-list {
  margin: 0;
  display: grid;
  gap: 12px;
}

.meta-list div {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  border-bottom: 1px solid #edf2f7;
  padding-bottom: 8px;
}

.meta-list dt {
  color: #475569;
}

.meta-list dd {
  margin: 0;
  font-weight: 700;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 10px 8px;
  border-bottom: 1px solid #edf2f7;
}

@media (max-width: 820px) {
  .content-grid,
  .bottom-grid {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }

  .candidate-columns {
    grid-template-columns: 1fr;
  }
}
