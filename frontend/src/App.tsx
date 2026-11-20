import { useState } from "react";
import FounderDashboard from "./pages/FounderDashboard";
import InvestorDashboard from "./pages/InvestorDashboard";

export default function App() {
  const [view, setView] = useState<"founder" | "investor">("founder");
  return (
    <div style={{ fontFamily: "sans-serif", padding: 24 }}>
      <h1>Fundability Platform</h1>
      <button onClick={() => setView("founder")}>Founder</button>{" "}
      <button onClick={() => setView("investor")}>Investor</button>
      {view === "founder" ? <FounderDashboard /> : <InvestorDashboard />}
    </div>
  );
}
