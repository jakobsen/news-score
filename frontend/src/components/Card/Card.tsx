import "./Card.css";

interface Props {
  children: React.ReactNode;
  className?: string;
}

export function Card({ children }: Props) {
  return <div className="card">{children}</div>;
}
