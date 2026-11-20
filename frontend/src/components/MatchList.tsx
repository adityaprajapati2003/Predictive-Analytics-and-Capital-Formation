export default function MatchList({ items }: { items: { name: string; compatibility: number }[] }) {
  return (<ul>{items.map((m) => <li key={m.name}>{m.name}: {m.compatibility.toFixed(2)}</li>)}</ul>);
}
