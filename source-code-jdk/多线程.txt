start源码
public synchronized void start() {
    // 如果线程不是"就绪状态"，则抛出异常！
    if (threadStatus != 0)
        throw new IllegalThreadStateException();
    // 将线程添加到ThreadGroup中
    group.add(this);
    boolean started = false;
    try {
        // 通过start0()启动线程
        start0();
        // 设置started标记
        started = true;
    } finally {
        try {
            if (!started) {
                group.threadStartFailed(this);
            }
        } catch (Throwable ignore) {
        }
    }
}

run源码
public void run() {
    if (target != null) {
        target.run();
    }
}

start: 启动一个新的线程，新线程调用 run 方法。start 不能重复调用。
run：和普通方法一样，可以重复调用。但是并不会启动新线程。


join源码
public final synchronized void join(long millis)
throws InterruptedException {
    long base = System.currentTimeMillis();
    long now = 0;
    if (millis < 0) {
        throw new IllegalArgumentException("timeout value is negative");
    }
    if (millis == 0) {
        while (isAlive()) { // isAlive() 通过子线程调用，则判断的就是子线程
            wait(0); // 等待的是当前线程（CPU 正则运行的线程），而不是子线程！
        }
    } else {
        while (isAlive()) {
            long delay = millis - now;
            if (delay <= 0) {
                break;
            }
            wait(delay);
            now = System.currentTimeMillis() - base;
        }
    }
}
join主要用来让“主线程”等待“子线程”结束之后才能继续运行。


实现多线程两种方式:继承Thread类 实现Runnable接口
因为Thread 是类，一个类只能有一个父类，但是可以有多个接口。Runnable有更好的扩展性。所以优先使用Runnable接口。