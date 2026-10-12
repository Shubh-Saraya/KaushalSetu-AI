import { useEffect, useMemo, useState } from 'react';

type Role = 'worker' | 'assessor' | 'admin';

type User = {
  id: number;
  name: string;
  email: string;
  role: Role;
  language: string;
};

type Qualification = {
  code: string;
  title: string;
  nsqf_level: string;
  score: number;
  explanation: string;
  matched_criteria: string[];
  missing_information: string[];
  verification_status: string;
};

const demoUsers = [
  { email: 'worker@demo.local', password: 'demo123', role: 'worker' as const },
  { email: 'assessor@demo.local', password: 'demo123', role: 'assessor' as const },
  { email: 'admin@demo.local', password: 'demo123', role: 'admin' as const },
];

function App() {
  const [user, setUser] = useState<User | null>(null);
  const [email, setEmail] = useState('worker@demo.local');
  const [password, setPassword] = useState('demo123');
  const [qualifications, setQualifications] = useState<Qualification[]>([]);

  useEffect(() => {
    setQualifications([
      {
        code: 'QP-ELC-01',
        title: 'Electrician General (Demonstration)',
        nsqf_level: 'Level 4',
        score: 92,
        explanation: 'The profile indicates electrical installation, switchboard work, and testing tasks. This is a relevance indicator, not proof of competence or certification.',
        matched_criteria: ['Tool identification', 'Electrical safety', 'Wiring installation'],
        missing_information: ['Fault diagnosis evidence', 'Live testing records'],
        verification_status: 'Demonstration record; requires official verification.',
      },
      {
        code: 'QP-WIRE-02',
        title: 'Domestic Wiring Technician',
        nsqf_level: 'Level 3',
        score: 74,
        explanation: 'This pack is relevant for residential and small commercial wiring tasks. Human review remains mandatory before final recommendation.',
        matched_criteria: ['Basic wiring layout', 'Switchboard installation'],
        missing_information: ['Supervisor witness statement', 'Safety checklist'],
        verification_status: 'Demonstration record; requires official verification.',
      },
    ]);
  }, []);

  const login = () => {
    const found = demoUsers.find((entry) => entry.email === email && entry.password === password);
    if (!found) {
      alert('Invalid demo credentials');
      return;
    }

    setUser({
      id: found.role === 'worker' ? 1 : found.role === 'assessor' ? 2 : 3,
      name: found.role === 'worker' ? 'Asha Worker' : found.role === 'assessor' ? 'Rahul Assessor' : 'Meera Admin',
      email,
      role: found.role,
      language: found.role === 'worker' ? 'Hindi' : 'English',
    });
  };

  const statCards = useMemo(() => {
    if (!user) return [];
    if (user.role === 'worker') {
      return [
        { label: 'Application status', value: 'Submitted' },
        { label: 'Trade', value: 'Electrician' },
        { label: 'Experience', value: '6 years' },
        { label: 'AI match', value: '92%' },
      ];
    }
    if (user.role === 'assessor') {
      return [
        { label: 'Assigned workers', value: '12' },
        { label: 'Pending assessments', value: '4' },
        { label: 'Completed', value: '9' },
        { label: 'Review queue', value: '2' },
      ];
    }
    return [
      { label: 'Registered workers', value: '14' },
      { label: 'Completed assessments', value: '9' },
      { label: 'Pending review', value: '4' },
      { label: 'Flagged cases', value: '2' },
    ];
  }, [user]);

  if (!user) {
    return (
      <div className="auth-shell">
        <div className="auth-card">
          <div className="brand-row">
            <div className="brand-mark">KS</div>
            <div>
              <p className="eyebrow">Smart India Hackathon 2026</p>
              <h1>KaushalSetu AI</h1>
            </div>
          </div>

          <div className="login-panel">
            <h2>Secure login</h2>
            <label>
              Email
              <input value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <label>
              Password
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <button onClick={login}>Login</button>
            <p className="demo-copy">Demo logins: worker@demo.local / demo123, assessor@demo.local / demo123, admin@demo.local / demo123</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">KaushalSetu AI</p>
          <h2>{user.role === 'worker' ? 'Worker dashboard' : user.role === 'assessor' ? 'Assessor workspace' : 'Administrator analytics'}</h2>
        </div>
        <button className="secondary-button" onClick={() => setUser(null)}>Logout</button>
      </header>

      <section className="stats-grid">
        {statCards.map((item) => (
          <div key={item.label} className="stat-card">
            <span>{item.label}</span>
            <strong>{item.value}</strong>
          </div>
        ))}
      </section>

      <section className="content-grid">
        <div className="panel wide-panel">
          <div className="panel-header">
            <h3>Qualification-pack matching</h3>
            <span className="pill warning">AI suggestions</span>
          </div>

          <div className="candidate-list">
            {qualifications.map((item) => (
              <div key={item.code} className="candidate-card">
                <div className="candidate-head">
                  <div>
                    <small>{item.code}</small>
                    <h4>{item.title}</h4>
                  </div>
                  <div className="score-box">{item.score}</div>
                </div>
                <p>{item.explanation}</p>
                <div className="candidate-columns">
                  <div>
                    <small>Matched criteria</small>
                    <ul>
                      {item.matched_criteria.map((criterion) => <li key={criterion}>{criterion}</li>)}
                    </ul>
                  </div>
                  <div>
                    <small>Missing evidence</small>
                    <ul>
                      {item.missing_information.map((criterion) => <li key={criterion}>{criterion}</li>)}
                    </ul>
                  </div>
                </div>
                <div className="meta-row">
                  <span>NSQF: {item.nsqf_level}</span>
                  <span>{item.verification_status}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="panel">
          <div className="panel-header">
            <h3>Profile snapshot</h3>
            <span className="pill success">Submitted</span>
          </div>
          <dl className="meta-list">
            <div><dt>Worker ID</dt><dd>KS-2026001</dd></div>
            <div><dt>Preferred language</dt><dd>Hindi</dd></div>
            <div><dt>State / District</dt><dd>Maharashtra / Nagpur</dd></div>
            <div><dt>Primary trade</dt><dd>Electrician</dd></div>
            <div><dt>Years of experience</dt><dd>6</dd></div>
          </dl>
        </div>
      </section>

      <section className="bottom-grid">
        <div className="panel">
          <div className="panel-header">
            <h3>Assessment rubric</h3>
            <span className="pill neutral">Electrician</span>
          </div>
          <table>
            <thead>
              <tr>
                <th>Criterion</th>
                <th>Score</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>Tool identification</td><td>3</td><td>Satisfactory</td></tr>
              <tr><td>Safety compliance</td><td>2</td><td>Satisfactory</td></tr>
              <tr><td>Wiring task execution</td><td>2</td><td>Satisfactory</td></tr>
              <tr><td>Fault diagnosis</td><td>1</td><td>Insufficient evidence</td></tr>
            </tbody>
          </table>
        </div>

        <div className="panel">
          <div className="panel-header">
            <h3>AI assistance panel</h3>
            <span className="pill warning">Human review required</span>
          </div>
          <ul className="bullet-list">
            <li>Summarises evidence: installation photos and supervisor checklist available.</li>
            <li>Identifies missing evidence: fault-finding log and live testing records.</li>
            <li>Suggests follow-up: request direct evidence of safe handling and testing procedure.</li>
            <li>Flags inconsistency: incomplete evidence should not trigger final certification.</li>
          </ul>
        </div>
      </section>
    </div>
  );
}

export default App;
