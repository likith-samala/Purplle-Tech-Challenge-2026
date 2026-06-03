"use client";

import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    axios.get("https://purplle-tech-challenge-2026.onrender.com/report")
      .then((res) => setReport(res.data))
      .catch((err) => console.log(err));
  }, []);

  if (!report) {
    return (
      <div className="p-10">
        <h1 className="text-3xl font-bold">Loading Dashboard...</h1>
      </div>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-100 to-blue-100 p-10 text-black">

      <h1 className="text-5xl font-bold mb-3">
        AI Store Intelligence Dashboard
      </h1>

      <p className="text-gray-700 text-lg mb-10">
        AI-powered Store Intelligence System using CCTV footage for
        customer analytics, footfall monitoring, people counting,
        tracking, and heatmap generation.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">Camera</h2>
          <p className="text-5xl font-bold text-blue-700">
            {report.camera}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">
            Frames Processed
          </h2>
          <p className="text-5xl font-bold text-blue-600">
            {report.framesProcessed}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">
            Total Person Detections
          </h2>
          <p className="text-5xl font-bold text-purple-600">
            {report.totalPersonDetections}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">
            Average People Visible
          </h2>
          <p className="text-5xl font-bold text-orange-500">
            {report.averagePeopleVisible}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">
            Maximum People Visible
          </h2>
          <p className="text-5xl font-bold text-red-500">
            {report.maxPeopleVisible}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow-lg border hover:shadow-2xl transition-all">
          <h2 className="font-bold text-xl mb-3">
            System Status
          </h2>
          <p className="text-5xl font-bold text-green-600 uppercase">
            {report.status}
          </p>
        </div>

      </div>

      {/* Heatmap Section */}
      <div className="mt-10 bg-white p-6 rounded-2xl shadow-lg border">
        <h2 className="text-3xl font-bold mb-5">
          Customer Heatmap
        </h2>

        <img
          src="/heatmap_cam1.png"
          alt="Customer Heatmap"
          className="rounded-xl w-full shadow"
        />
      </div>

      {/* Footer */}
      <footer className="mt-10 text-center text-gray-600">
        <p className="font-semibold">
          Purplle Tech Challenge 2026
        </p>

        <p>
          AI Store Intelligence System using YOLOv8, FastAPI and Next.js
        </p>
      </footer>

    </main>
  );
}