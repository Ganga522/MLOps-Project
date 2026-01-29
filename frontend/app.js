const API = "http://localhost:8000";

async function load(){
  const f = await fetch(API+"/metrics/factory").then(r=>r.json());
  const w = await fetch(API+"/metrics/workers").then(r=>r.json());
  const s = await fetch(API+"/metrics/workstations").then(r=>r.json());

  // Factory
  document.getElementById('factory').innerHTML = `
    <div class="metric-card">
      <div class="metric-title">Total Productive Time</div>
      <div class="metric-value">${f.total_productive_time}</div>
    </div>
    <div class="metric-card">
      <div class="metric-title">Total Production</div>
      <div class="metric-value">${f.total_production}</div>
    </div>
    <div class="metric-card">
      <div class="metric-title">Avg Utilization</div>
      <div class="metric-value">${f.average_utilization}</div>
    </div>
    <div class="metric-card">
      <div class="metric-title">System Status</div>
      <div class="metric-value">Active</div>
    </div>
  `;

  // Workers
  document.getElementById('workers').innerHTML = "";
  for(let k in w){
    document.getElementById('workers').innerHTML += `
      <div class="card">
        <h3>${k} <span class="badge">Worker</span></h3>
        <div class="data-row"><span>Active Time</span><span>${w[k].active}</span></div>
        <div class="data-row"><span>Idle Time</span><span>${w[k].idle}</span></div>
        <div class="data-row"><span>Units Produced</span><span>${w[k].units}</span></div>
      </div>
    `;
  }

  // Stations
  document.getElementById('stations').innerHTML = "";
  for(let k in s){
    document.getElementById('stations').innerHTML += `
      <div class="card">
        <h3>${k} <span class="badge">Station</span></h3>
        <div class="data-row"><span>Occupancy</span><span>${s[k].occupancy}</span></div>
        <div class="data-row"><span>Units Produced</span><span>${s[k].units}</span></div>
      </div>
    `;
  }
}

load();
