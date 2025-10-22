import { useState } from "react";
import "./App.css";
import { Button } from "./components/Button";
import { Input } from "./components/Input";

function App() {
  const [temperature, setTemperature] = useState("");
  const [heartRate, setHeartRate] = useState("");
  const [respiratoryRate, setRespiratoryRate] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
  };

  const handleReset = () => {
    setTemperature("");
    setHeartRate("");
    setRespiratoryRate("");
  };

  return (
    <main>
      <h1>NEWS score calculator</h1>
      <form onSubmit={handleSubmit}>
        <Input
          id="body-temp"
          label="Body temperature"
          subLabel="Degrees celcius"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <Input
          id="heart-rate"
          label="Heartrate"
          subLabel="Beats per minute"
          value={heartRate}
          onChange={(e) => setHeartRate(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <Input
          id="respiratory-rate"
          label="Respiratory rate"
          subLabel="Breaths per minute"
          value={respiratoryRate}
          onChange={(e) => setRespiratoryRate(e.target.value)}
          type="number"
          inputMode="numeric"
        />
        <div className="actions">
          <Button>Calculate NEWS score</Button>
          <Button type="reset" variant="secondary" onClick={handleReset}>
            Reset form
          </Button>
        </div>
      </form>
    </main>
  );
}

export default App;
