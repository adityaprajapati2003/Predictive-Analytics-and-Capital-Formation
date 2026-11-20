import ScoreCard from "../components/ScoreCard";
import UploadDeck from "../components/UploadDeck";

export default function FounderDashboard() {
  return (
    <section>
      <h2>Founder dashboard</h2>
      <UploadDeck />
      <ScoreCard probability={null} />
    </section>
  );
}
