FROM python:3.10-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends git ruby-full curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev nodejs graphviz graphviz-dev && rm -rf /var/lib/apt/lists/*
RUN pip install requests tqdm pygraphviz networkx Pillow
RUN export GEM_HOME="$HOME/gems"
RUN export PATH="$HOME/gems/bin:$PATH"
WORKDIR /project
RUN gem install jekyll bundler
COPY Gemfile Gemfile.lock jekyll-theme-yat.gemspec ./
RUN bundle install
RUN curl -fsSL https://github.com/Pagefind/pagefind/releases/download/v1.5.2/pagefind-v1.5.2-x86_64-unknown-linux-musl.tar.gz -o /tmp/pagefind.tar.gz \
    && tar -xzf /tmp/pagefind.tar.gz -C /usr/local/bin pagefind \
    && chmod +x /usr/local/bin/pagefind \
    && rm /tmp/pagefind.tar.gz
