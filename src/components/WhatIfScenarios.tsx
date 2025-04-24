"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useDashboardContext } from "@/contexts/dashboard-context";
import { useToast } from "@/hooks/use-toast";

export const WhatIfScenarios = () => {
  const [messages, setMessages] = useState<
    { sender: "user" | "ai"; text: string }[]
  >([]);
  const [currentQuery, setCurrentQuery] = useState("");
  const { addQuery } = useDashboardContext();
  const { toast } = useToast();

  const handleAskWicketWise = () => {
    if (currentQuery.trim() === "") return;

    // Add user's query to the chat
    setMessages([...messages, { sender: "user", text: currentQuery }]);

    // Simulate AI response
    setTimeout(() => {
      const aiResponse = `This is a hypothetical analysis based on "${currentQuery}".`;
      setMessages([...messages, { sender: "user", text: currentQuery }, { sender: "ai", text: aiResponse }]);

      // Save scenario
      addQuery({
        query: currentQuery,
        response: aiResponse,
      });
      toast({
        title: "Scenario Saved",
        description: "Scenario saved to your history.",
      });
    }, 500);

    setCurrentQuery("");
  };

  const handleSaveScenario = () => {
    // TODO: Implement save functionality
    // The save functionality is already implemented in handleAskWicketWise
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

      </CardContent>
    </Card>
  );
};
