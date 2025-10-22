import "./Button.css";

interface Props
  extends Omit<React.ButtonHTMLAttributes<HTMLButtonElement>, "className"> {
  variant?: "primary" | "secondary";
}

export function Button({ children, variant = "primary", ...delegated }: Props) {
  return (
    <button className={variant} {...delegated}>
      {children}
    </button>
  );
}
