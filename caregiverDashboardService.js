// caregiverDashboardService.js

class CaregiverDashboardService {
  constructor() {
    this.engine = window.insightEngine || null;
  }

  getWeeklyTrend() {
    return {
      highestRiskDay: "Thursday",
      averageNightlyRisk: "Medium-High",
      totalAnomalies: 8
    };
  }

  getEmergencyEvents() {
    return [
      { id: 101, time: "Yesterday, 11:30 PM", factor: "Ignored missed meal warning", solved: true },
      { id: 102, time: "3 days ago, 2:15 AM", factor: "Post-workout dehydration", solved: false },
      { id: 103, time: "5 days ago, 10:00 PM", factor: "High pulse instability", solved: true }
    ];
  }

  getComplianceData() {
    return [
      { metric: "Missed Bedtime Scans", count: 2, limit: 3 },
      { metric: "Ignored Hydration Reminders", count: 4, limit: 5 },
      { metric: "Long Fasting Events", count: 1, limit: 2 }
    ];
  }

  getDocumentSummaries() {
    return [
      { date: "Oct 12, 2025", notes: "Dr. Smith: Increase evening complex carbs. Avoid strenuous exercise after 8 PM." },
      { date: "Sep 28, 2025", notes: "Cardiology Review: Pulse baseline updated. Normal variability confirmed during light activity." }
    ];
  }

  getNightChartData() {
    return {
      labels: ["10PM", "11PM", "12AM", "1AM", "2AM", "3AM"],
      values: [20, 35, 60, 85, 40, 15] // Mock anomaly probability curve
    };
  }
}

window.caregiverService = new CaregiverDashboardService();
