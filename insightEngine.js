// insightEngine.js

class InsightEngine {
  constructor() {
    this.triggers = ['evening workouts', 'skipped meals', 'late lunches', 'poor sleep nights', 'dehydration'];
    this.history = this.generateRealisticMockData();
  }

  generateRealisticMockData() {
    const data = [];
    const now = Date.now();
    const dayMs = 24 * 60 * 60 * 1000;
    
    for(let i = 30; i >= 0; i--) {
      // 2 scans a day
      const date1 = new Date(now - i * dayMs);
      date1.setHours(8 + Math.floor(Math.random() * 2)); // Morning
      
      const date2 = new Date(now - i * dayMs);
      date2.setHours(19 + Math.floor(Math.random() * 4)); // Evening/night
      
      // Add anomaly based on random trigger
      const hasAnomaly = Math.random() > 0.7;
      let riskScore = 0.2 + Math.random() * 0.2; // Low risk default
      let trigger = null;
      
      if(hasAnomaly) {
        riskScore = 0.6 + Math.random() * 0.35; // Medium to High
        trigger = this.triggers[Math.floor(Math.random() * this.triggers.length)];
      }

      data.push({ timestamp: date1.getTime(), riskScore: riskScore * 0.8, trigger: null });
      data.push({ timestamp: date2.getTime(), riskScore, trigger });
    }
    return data;
  }

  getSmartCards() {
    return [
      { id: 1, text: "Your anomaly risk increases 2.1x after evening workouts", type: "workout" },
      { id: 2, text: "Late lunch delays repeatedly increase blink instability", type: "meal" },
      { id: 3, text: "Night scans after 11 PM show higher pulse deviation", type: "time" },
      { id: 4, text: "Poor sleep correlates with reduced face stability", type: "sleep" }
    ];
  }

  getRecommendations() {
    return [
      { title: "Safer Workout Windows", desc: "Shift workouts to morning hours to avoid post-exercise late pulse spikes." },
      { title: "Snack Timing Reminder", desc: "Avoid gaps longer than 5 hours. A complex carbohydrate snack at 4 PM is recommended." },
      { title: "Bedtime Hydration", desc: "Ensure at least 2 glasses of water after 8 PM to prevent morning dehydration anomalies." }
    ];
  }

  getChartData() {
    // Risk over time (last 7 days mapping)
    const labels = [];
    const values = [];
    const recent = this.history.slice(-14);
    recent.forEach(r => {
      labels.push(new Date(r.timestamp).toLocaleDateString(undefined, {month:'short', day:'numeric'}));
      values.push(Math.round(r.riskScore * 100));
    });

    const triggerFreq = {};
    this.triggers.forEach(t => triggerFreq[t] = 0);
    this.history.forEach(r => {
      if(r.trigger) triggerFreq[r.trigger]++;
    });

    return {
      riskTrend: { labels, values },
      triggers: Object.keys(triggerFreq).map(k => ({ name: k, count: triggerFreq[k] }))
    };
  }
}

window.insightEngine = new InsightEngine();
