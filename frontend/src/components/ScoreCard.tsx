export default function ScoreCard({ probability }: { probability: number | null }) {
  return (
    <div>
      <h3>Funding probability (12 months)</h3>
      <p>{probability === null ? "No score yet" : `${(probability * 100).toFixed(0)}%`}</p>
      <small>Calibrated estimate, not a guarantee. Compatibility scores are separate.</small>
    </div>
  );
}
