```jsx
import { useState } from “react”;

export default function ClipEditor({ clip, onExportAll, videoUrl }) {
const [startTime, setStartTime] = useState(clip.start);
const [endTime, setEndTime] = useState(clip.end);
const [caption, setCaption] = useState(clip.transcript);
const [musicVolume, setMusicVolume] = useState(50);
const [exporting, setExporting] = useState(false);

const handleExportClip = async () => {
setExporting(true);
try {
// In real app: call backend /generate-clip endpoint
// For MVP: simulate with alert
alert(`Exporting clip “${clip.id.slice(0, 6)}”\nStart: ${startTime}s
