import "./Input.css";
import { useId } from "react";

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  subLabel?: string;
  id?: string;
}

export function Input({ label, subLabel, id, ...delegated }: Props) {
  const generatedId = useId();
  const appliedId = id ?? generatedId;
  return (
    <>
      <div>
        <label htmlFor={appliedId}>
          <span className="main-label">{label}</span>
          {subLabel && <span className="sub-label">{subLabel}</span>}
        </label>
        <input {...delegated} id={appliedId} />
      </div>
    </>
  );
}
