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

const workerProfile = {
  workerId: 'KS-2026001',
  trade: 'Electrician',
  language: 'Hindi',
  state: 'Maharashtra',
  district: 'Nagpur',
  age: 29,
  yearsExp: 6,
  type: 'Daily wage',
  tasks: ['Switchboard installation', 'MCB replacement', 'Basic wiring repairs', 'Testing continuity'],
  tools: ['Multimeter', 'Screwdrivers', 'Pliers', 'Electrical test lamp'],
  evidence: [
    { label: 'Safety checklist', status: 'Verified' },
    { label: 'Installation photos', status: 'Uploaded' },
    { label: 'Fault diagnosis log', status: 'Missing evidence' },
  ],
};

const rubricRows = [
  { criterion: 'Tool identification', score: 3, status: 'Satisfactory' },
  { criterion: 'Electrical safety', score: 2, status: 'Satisfactory' },
  { criterion: 'Wiring execution', score: 2, status: 'Satisfactory' },
  { criterion: 'Fault diagnosis', score: 1, status: 'Insufficient evidence' },
];

function App() {
  const [user, setUser] = useState<User | null>(null);
  const [email, setEmail] = useState('worker@demo.local');
  const [password, setPassword] = useState('demo123');
  const [activeTab, setActiveTab] = useState('Overview');
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

  const tabs = useMemo(() => {
    if (!user) return ['Login'];
    if (user.role === 'worker') return ['Overview', 'Profile', 'Evidence', 'Qualifications'];
    if (user.role === 'assessor') return ['Overview', 'Assignments', 'Rubric', 'AI Assistance'];
    return ['Overview', 'Analytics', 'Assessments', 'Records'];
  }, [user]);

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
    setActiveTab('Overview');
  };

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
    <div className="dashboard-shell">
      <aside className="sidebar">
        <div className="brand-block">
          <div className="brand-mark small">KS</div>
          <div>
            <p className="eyebrow">KaushalSetu</p>
            <strong>AI RPL Suite</strong>
          </div>
        </div>

        <nav className="nav-list">
          {tabs.map((tab) => (
            <button
              key={tab}
              className={activeTab === tab ? 'nav-button active' : 'nav-button'}
              onClick={() => setActiveTab(tab)}
            >
              {tab}
            </button>
          ))}
        </nav>

        <div className="profile-mini">
          <strong>{user.name}</strong>
          <span>{user.role}</span>
        </div>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div>
            <p className="eyebrow">Dashboard</p>
            <h2>{user.role === 'worker' ? 'Worker workspace' : user.role === 'assessor' ? 'Assessor dashboard' : 'Administrator analytics'}</h2>
          </div>
          <button className="secondary-button" onClick={() => setUser(null)}>Logout</button>
        </header>

        <section className="stats-grid">
          {statCards.map((card) => (
            <div key={card.label} className="stat-card">
              <span>{card.label}</span>
              <strong>{card.value}</strong>
            </div>
          ))}
        </section>

        {activeTab === 'Overview' && (
          <div className="content-grid">
            <div className="panel wide-panel">
              <div className="panel-header">
                <h3>AI qualification mapping</h3>
                <span className="pill warning">Suggestions only</span>
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
                <div><dt>Worker ID</dt><dd>{workerProfile.workerId}</dd></div>
                <div><dt>Trade</dt><dd>{workerProfile.trade}</dd></div>
                <div><dt>Language</dt><dd>{workerProfile.language}</dd></div>
                <div><dt>Location</dt><dd>{workerProfile.state} / {workerProfile.district}</dd></div>
                <div><dt>Experience</dt><dd>{workerProfile.yearsExp} years</dd></div>
              </dl>
            </div>
          </div>
        )}

        {activeTab === 'Profile' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Worker profile</h3>
              <span className="pill neutral">Guided application</span>
            </div>
            <div className="form-grid">
              <div className="field"><label>Worker ID</label><input value={workerProfile.workerId} readOnly /></div>
              <div className="field"><label>Name</label><input value="Asha Worker" readOnly /></div>
              <div className="field"><label>Age</label><input value={workerProfile.age} readOnly /></div>
              <div className="field"><label>Preferred language</label><input value={workerProfile.language} readOnly /></div>
              <div className="field"><label>State</label><input value={workerProfile.state} readOnly /></div>
              <div className="field"><label>District</label><input value={workerProfile.district} readOnly /></div>
              <div className="field wide"><label>Primary trade</label><input value={workerProfile.trade} readOnly /></div>
              <div className="field"><label>Years of experience</label><input value={workerProfile.yearsExp} readOnly /></div>
              <div className="field"><label>Employment type</label><input value={workerProfile.type} readOnly /></div>
              <div className="field wide"><label>Tasks regularly performed</label><textarea value={workerProfile.tasks.join(', ')} readOnly /></div>
              <div className="field wide"><label>Tools and equipment used</label><textarea value={workerProfile.tools.join(', ')} readOnly /></div>
            </div>
          </div>
        )}

        {activeTab === 'Evidence' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Evidence submission</h3>
              <span className="pill warning">Review required</span>
            </div>
            <div className="evidence-list">
              {workerProfile.evidence.map((item) => (
                <div key={item.label} className="evidence-item">
                  <span>{item.label}</span>
                  <strong className={item.status === 'Missing evidence' ? 'status warning' : 'status good'}>{item.status}</strong>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'Assignments' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Assigned workers</h3>
              <span className="pill neutral">3 pending</span>
            </div>
            <table>
              <thead>
                <tr>
                  <th>Worker</th>
                  <th>Trade</th>
                  <th>Status</th>
                  <th>Progress</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>Asha Worker</td><td>Electrician</td><td>Under review</td><td>82%</td></tr>
                <tr><td>Rajesh Kumar</td><td>Welder</td><td>Practical assessment</td><td>58%</td></tr>
                <tr><td>Sanjana Patil</td><td>Plumber</td><td>Draft</td><td>34%</td></tr>
              </tbody>
            </table>
          </div>
        )}

        {activeTab === 'Rubric' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Criterion-based assessment</h3>
              <span className="pill success">Electrician</span>
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
                {rubricRows.map((row) => (
                  <tr key={row.criterion}>
                    <td>{row.criterion}</td>
                    <td>{row.score}</td>
                    <td>{row.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {activeTab === 'AI Assistance' && (
          <div className="panel">
            <div className="panel-header">
              <h3>AI assistance panel</h3>
              <span className="pill warning">Human review required</span>
            </div>
            <ul className="bullet-list">
              <li>Summaries evidence: installation photos and supervisor checklist available.</li>
              <li>Identifies missing evidence: fault-finding log and live testing records.</li>
              <li>Suggests follow-up: request direct evidence of safe handling and testing procedure.</li>
              <li>Flags inconsistency: incomplete evidence should not trigger final certification.</li>
            </ul>
          </div>
        )}

        {activeTab === 'Analytics' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Administrator analytics</h3>
              <span className="pill neutral">Synthetic demo</span>
            </div>
            <div className="analytics-grid">
              <div><span>Registered workers</span><strong>14</strong></div>
              <div><span>Assessments completed</span><strong>9</strong></div>
              <div><span>Pending reviews</span><strong>4</strong></div>
              <div><span>Average completion</span><strong>3.4 days</strong></div>
            </div>
          </div>
        )}

        {activeTab === 'Assessments' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Assessment records</h3>
              <span className="pill neutral">Recent</span>
            </div>
            <table>
              <thead>
                <tr>
                  <th>Reference</th>
                  <th>Trade</th>
                  <th>Recommendation</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>AS-1001</td><td>Electrician</td><td>Recommended for review</td><td>Completed</td></tr>
                <tr><td>AS-1042</td><td>Welder</td><td>Requires evidence</td><td>Pending</td></tr>
              </tbody>
            </table>
          </div>
        )}

        {activeTab === 'Records' && (
          <div className="panel">
            <div className="panel-header">
              <h3>Verification notices</h3>
              <span className="pill warning">Official validation needed</span>
            </div>
            <ul className="bullet-list">
              <li>Qualification records shown here are demonstration data and require official verification.</li>
              <li>AI matches are relevance indicators only.</li>
              <li>Final certification decisions remain with authorised human assessors and certification authority.</li>
            </ul>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
