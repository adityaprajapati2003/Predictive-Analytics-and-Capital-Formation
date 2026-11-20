import { Bar, BarChart, XAxis, YAxis } from "recharts";

export default function ShapChart({ data }: { data: { feature: string; contribution: number }[] }) {
  return (
    <BarChart width={420} height={220} data={data} layout="vertical">
      <XAxis type="number" /><YAxis type="category" dataKey="feature" width={140} />
      <Bar dataKey="contribution" />
    </BarChart>
  );
}
