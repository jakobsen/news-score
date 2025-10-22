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
    <label htmlFor={appliedId}>
      {label}
      {subLabel && (
        <>
          <br />
          <span>{subLabel}</span>
        </>
      )}
      <input {...delegated} id={appliedId} />
    </label>
  );
}
