#!/usr/bin/env bash

# bigsbetal.cfd — деплой в GitHub + Cloudflare Pages (один проект, все языки)
# Использование: CLOUDFLARE_API_TOKEN="xxx" ./deploy.sh

ROOT_DOMAIN="bigsbetal.cfd"
GITHUB_USERNAME="bigsbettest"
REPO_NAME="bigsbetal-cfd"
PROJECT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CF_ACCOUNT_ID="311ad24e30a4dd6f3d13ab5f6c48e0d4"
CF_API_TOKEN="${CLOUDFLARE_API_TOKEN}"
export CLOUDFLARE_ACCOUNT_ID="${CF_ACCOUNT_ID}"
export CLOUDFLARE_API_TOKEN="${CF_API_TOKEN}"

# Все домены: основной + поддомены по языкам
DOMAINS="${ROOT_DOMAIN} ru.${ROOT_DOMAIN} en.${ROOT_DOMAIN} de.${ROOT_DOMAIN} pl.${ROOT_DOMAIN} uz.${ROOT_DOMAIN} az.${ROOT_DOMAIN} ky.${ROOT_DOMAIN}"

# Проверки
command -v gh >/dev/null 2>&1 || { echo "ОШИБКА: Установите GitHub CLI (gh)"; exit 1; }
command -v wrangler >/dev/null 2>&1 || { echo "ОШИБКА: Установите Wrangler (npm i -g wrangler)"; exit 1; }
if [ -z "${CF_API_TOKEN}" ]; then
  echo "ОШИБКА: Установите CLOUDFLARE_API_TOKEN"
  echo "  export CLOUDFLARE_API_TOKEN=\"ваш_токен\""
  exit 1
fi

echo "=== bigsbetal.cfd — Деплой ==="
echo "Домен: https://${ROOT_DOMAIN} (+ ru, en, de, pl, uz, az, ky)"
echo "Путь: ${PROJECT_PATH}"
echo ""

echo "=== ЭТАП 1: GITHUB ==="
gh repo create "${GITHUB_USERNAME}/${REPO_NAME}" --public --description "BigsBet satellite ${ROOT_DOMAIN}" 2>/dev/null || echo "  Репо уже существует"
cd "${PROJECT_PATH}"
rm -rf .git 2>/dev/null
git init
git add .
git commit -m "Deploy: guides AZ/KY translations, See also blocks" 2>/dev/null || git commit --allow-empty -m "Deploy"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
git push -u origin main --force || { echo "ОШИБКА: Push"; exit 1; }
echo "  ✓ GitHub: ${REPO_NAME}"
echo ""

echo "=== ЭТАП 2: CLOUDFLARE PAGES ==="
wrangler pages project create "${REPO_NAME}" --production-branch main 2>/dev/null || echo "  Проект уже существует"
sleep 2
wrangler pages deploy "${PROJECT_PATH}" --project-name="${REPO_NAME}" || { echo "ОШИБКА: Deploy"; exit 1; }
echo "  ✓ Deploy выполнен"
echo ""

echo "=== ЭТАП 3: Привязка доменов ==="
for DOM in ${DOMAINS}; do
  RES=$(curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/pages/projects/${REPO_NAME}/domains" \
    -H "Authorization: Bearer ${CF_API_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"${DOM}\"}")
  if echo "$RES" | grep -q '"success":true'; then
    echo "  ✓ ${DOM}"
  else
    echo "  (${DOM} — уже привязан или ошибка)"
  fi
done

echo ""
echo "=== ГОТОВО ==="
echo ""
echo "Сайты:"
echo "  https://${ROOT_DOMAIN} → ru"
echo "  https://ru.${ROOT_DOMAIN}"
echo "  https://en.${ROOT_DOMAIN}"
echo "  https://de.${ROOT_DOMAIN}"
echo "  https://pl.${ROOT_DOMAIN}"
echo "  https://uz.${ROOT_DOMAIN}"
echo "  https://az.${ROOT_DOMAIN}"
echo "  https://ky.${ROOT_DOMAIN}"
echo ""
