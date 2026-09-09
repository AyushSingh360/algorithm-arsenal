type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  private events: Map<string, Callback[]>;

  constructor() {
    this.events = new Map();
  }

  subscribe(eventName: string, callback: Callback): Subscription {
    if (!this.events.has(eventName)) {
      this.events.set(eventName, []);
    }

    const callbacks = this.events.get(eventName)!;
    callbacks.push(callback);

    return {
      unsubscribe: () => {
        const arr = this.events.get(eventName);
        if (!arr) return;

        const index = arr.indexOf(callback);
        if (index !== -1) {
          arr.splice(index, 1);
        }
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    const callbacks = this.events.get(eventName);
    if (!callbacks) return [];

    return callbacks.map((callback) => callback(...args));
  }
}
