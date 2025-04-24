"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const WhatIfScenarios = () => {
  const [messages, setMessages] = useState<
    { sender: "user" | "ai"; text: string }[]
  >([]);
  const [currentQuery, setCurrentQuery] = useState("");

  const handleAskWicketWise = () => {
    if (currentQuery.trim() === "") return;

    // Add user's query to the chat
    setMessages([...messages, { sender: "user", text: currentQuery }]);

    // Simulate AI response with disclaimer
    setTimeout(() => {
      const aiResponse = `This is a hypothetical analysis based on "${currentQuery}". This is for informational purposes only.`;
      setMessages([...messages, { sender: "user", text: currentQuery }, { sender: "ai", text: aiResponse }]);
    }, 500);

    setCurrentQuery("");
  };

  const handleSaveScenario = () => {
    // TODO: Implement save functionality
  };

  return (
    <Card className="space-y-4">
      <CardHeader>
        <CardTitle>🤔 What-If Scenarios</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="h-64 overflow-y-auto space-y-2">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`p-2 rounded-md ${
                message.sender === "user" ? "bg-secondary text-secondary-foreground self-end" : "bg-muted text-muted-foreground self-start"
              }`}
            >
              {message.text}
              {message.sender === "ai" && (
                <div className="mt-2 p-2 bg-accent text-accent-foreground rounded-md text-sm">
                  This is a hypothetical analysis based on past data and trends. It is not a prediction or guarantee of actual outcomes.
                </div>
              )}
            </div>
          ))}
        </div>
        <div className="flex space-x-2">
          <Input
            type="text"
            placeholder="Enter your scenario"
            value={currentQuery}
            onChange={(e) => setCurrentQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleAskWicketWise();
              }
            }}
          />
          <Button onClick={handleAskWicketWise}>Ask WicketWise</Button>
        </div>
        <Button variant="secondary" onClick={handleSaveScenario}>
          Save Scenario
        </Button>
      </CardContent>
    </Card>
  );
};
